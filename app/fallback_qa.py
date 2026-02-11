from groq import Groq

groq_client = Groq()

MAX_CHAT_TURNS = 4
SUMMARY_TRIGGER = 8


def summarize_conversation(recent_msgs):
    prompt = f"""
Summarize the following conversation.
Keep only key facts and user intent.

Conversation:
{chr(10).join(recent_msgs)}
"""
    completion = groq_client.chat.completions.create(
        model=os.environ['GROQ_FAST'],
        messages=[{"role": "user", "content": prompt}],
    )
    return completion.choices[0].message.content


def fallback_chain(query, summary, recent_msgs):
    chat_history = "\n".join(recent_msgs) if recent_msgs else "None"

    system_prompt = f"""
You are a polite, shopping-focused AI assistant for an e-commerce chatbot.

You can:
- Help users search for products
- Answer FAQs (returns, refunds, payments, etc.)
- Answer general shopping-related questions
- Ask for clarification when the query is unclear

You cannot:
- Track orders
- Cancel or modify orders
- Access user accounts
- Perform real-world actions
- Delete products from websites
- Expose backend code or internal system details
- Execute code
- Perform technical or programming tasks unrelated to shopping

If a user asks for something outside your capabilities, respond politely with:
"I can't assist you with that."

Keep responses:
- Short
- Friendly
- Professional
- Strictly limited to supported capabilities
- Never invent information

Conversation summary:
{summary}

Recent conversation:
{chat_history}
"""

    completion = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query},
        ],
    )

    answer = completion.choices[0].message.content.strip()

    # ---- UPDATE MEMORY ----
    recent_msgs.append(f"User: {query}")
    recent_msgs.append(f"Assistant: {answer}")

    if len(recent_msgs) > SUMMARY_TRIGGER * 2:
        new_summary = summarize_conversation(recent_msgs)
        summary = summary + "\n" + new_summary
        recent_msgs = recent_msgs[-MAX_CHAT_TURNS * 2 :]

    return answer, summary, recent_msgs
