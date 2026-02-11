import streamlit as st
from pathlib import Path
import importlib
import re

import router
import faq
import sql
import general_qa
import fallback_qa

st.set_page_config(
    page_title="E-Commerce AI Assistant",
    page_icon="🛍️",
    layout="centered"
)

if "modules_loaded" not in st.session_state:
    importlib.reload(faq)
    importlib.reload(sql)
    importlib.reload(general_qa)
    importlib.reload(fallback_qa)
    st.session_state.modules_loaded = True

if "data_loaded" not in st.session_state:
    faq_path = Path(__file__).parent / "resources/faq_data.csv"
    general_qa_path = Path(__file__).parent / "resources/ecommerce_chatbot_qna.csv"

    faq.ingest_faq_data(faq_path)
    general_qa.general_data_ingest(general_qa_path)

    st.session_state.data_loaded = True

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "👋 Hi! I’m your e-commerce assistant. Ask me about products, prices, offers, or comparisons."
        }
    ]

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "recent_messages" not in st.session_state:
    st.session_state.recent_messages = []

def force_sql(query: str) -> bool:
    q = query.lower()

    price_pattern = r"(under|below|less than)\s*\d+(\s?k)?|\brs\.?\s*\d+|\b₹\s*\d+"

    keywords = [
        "rated", "rating", "ratings", "reviews", "popular",
        "top rated", "best rated",
        "show me", "find", "list", "give me", "provide me"
    ]

    return (
        re.search(price_pattern, q) is not None
        or any(k in q for k in keywords)
    )

st.markdown(
    """
    <h1 style="text-align:center;">🛍️ E-Commerce Chatbot</h1>
    <p style="text-align:center; color:gray;">
    Ask about products, deals or shopping help
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
    div.stButton > button {
        font-size: 11px !important;
        padding: 4px 5px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("### 💡 Try asking:")

example_queries = [
    "provide iphone under 1 lakh?",
    "Find laptops below 80k?",
    "Which is the best rated shoes?",
    "What are the payment methods?"
]

cols = st.columns(2)

for i, example in enumerate(example_queries):
    if cols[i % 2].button(example):
        st.session_state.example_query = example

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

query = st.chat_input("Type your shopping question here...")

# Auto-trigger if example button clicked
if "example_query" in st.session_state:
    query = st.session_state.example_query
    del st.session_state.example_query

if query:
    with st.chat_message("user"):
        st.markdown(query)

    st.session_state.messages.append(
        {"role": "user", "content": query}
    )

    q_clean = query.lower().strip()

    try:
        if q_clean in {"thanks", "thank you", "ya thank you", "thx"}:
            answer = "😊 You're welcome! Let me know if you need help shopping."

        else:
            # ROUTING
            route_obj = router.router(query)

            if force_sql(query):
                route = "sql"
            elif route_obj is None:
                route = None
            else:
                route = route_obj.name

            # RESPONSE
            if route is None:
                answer = "I can't assist you with that"

            elif route == "faq":
                answer, new_summary, new_recent = fallback_qa.fallback_chain(
                    query=query,
                    summary=st.session_state.summary,
                    recent_msgs=st.session_state.recent_messages
                )
                st.session_state.summary = new_summary
                st.session_state.recent_messages = new_recent

            elif route == "sql":
                answer = sql.sql_chain(query)

            elif route == "general_qa":
                answer = general_qa.general_qa_chain(query)

            else:
                answer, new_summary, new_recent = fallback_qa.fallback_chain(
                    query=query,
                    summary=st.session_state.summary,
                    recent_msgs=st.session_state.recent_messages
                )
                st.session_state.summary = new_summary
                st.session_state.recent_messages = new_recent

    except Exception:
        answer = (
            "⚠️ I’m temporarily unavailable due to high traffic or system load. "
            "Please try again in a few minutes."
        )

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
