# 🛍️ AI-Powered E-Commerce Chatbot

A production-style AI assistant that integrates **LLM-powered Text-to-SQL**, **Retrieval-Augmented Generation (RAG)**, and **hybrid intent routing** to handle real-world shopping queries reliably and safely.

This project goes beyond prompt-based chatbots and focuses on:

- LLM system design  
- Structured data grounding  
- Production reliability  

---

# 🔗 Live Link

🔹 *Live App:** https://e-commerce-chatbot-czkqugwt9b9mfwwsk8dfbi.streamlit.app/
---

# 🚀 Engineering Highlights

- ✅ Hybrid semantic + rule-based intent routing  
- ✅ Schema-aware LLM Text-to-SQL pipeline  
- ✅ RAG-based FAQ system to prevent hallucinations  
- ✅ Session-isolated conversational memory (multi-user safe)  
- ✅ Defensive error handling for rate limits & API failures  
- ✅ Guardrails to prevent hallucinated SQL queries  
- ✅ Production-aware architecture design  

---

# 🔍 Core Capabilities

---

## 📊 1. Product Search (Text-to-SQL)

Converts natural language into SQL queries and executes them over a structured SQLite database.

### Features

- Schema-aware prompt design to prevent invalid column generation  
- Price filtering  
- Brand search (case-insensitive)  
- Rating thresholds  
- Popularity sorting (total ratings)  

### Example

```text
top rated mobiles under 20000
Nike shoes below 5000
```

---

## 📚 2. FAQ & Policy Handling (RAG)

Embedding-based vector retrieval using **ChromaDB** with context-grounded responses.

### Prevents

- Hallucinations  
- Fabricated policies  

### Handles

- Return & refund policies  
- Payment methods  
- Order tracking  
- Damaged product handling  

---

## 💬 3. General Conversational Assistance

- Handles assistant-related questions  
- Clarifies vague inputs  
- Redirects unsupported queries  
- Maintains contextual continuity per session  

---

# 🧠 System Architecture

```
User Query
    ↓
Hybrid Intent Router (Semantic + Rule-Based Guards)
    ↓
┌─────────────────────────────────────────────┐
│ Product Search                             │
│  → LLM Text-to-SQL                         │
│  → SQLite Execution                        │
│  → Structured LLM Response Formatting      │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ FAQ Handling (RAG)                         │
│  → Vector Search (ChromaDB)                │
│  → Context-Grounded LLM Response           │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ General Conversational Queries             │
│  → Instruction-Tuned LLM                   │
└─────────────────────────────────────────────┘
```

---

# 🛠 Tech Stack

- **Language:** Python  
- **Frontend:** Streamlit  
- **Database:** SQLite  
- **LLMs:** Groq-hosted LLaMA variants  
- **Routing:** Semantic Router  
- **Vector Store:** ChromaDB  
- **Embeddings:** Sentence Transformers  
- **Configuration:** dotenv  

---

# 📂 Project Structure

```
E-commerce_chatbot/
│
├── app/
│   ├── main.py              # Streamlit UI & routing orchestration
│   ├── router.py            # Semantic intent classification
│   ├── sql.py               # Text-to-SQL pipeline
│   ├── faq.py               # RAG-based FAQ system
│   ├── general_qa.py        # Conversational QA handling
│   ├── fallback_qa.py       # Safe fallback handling
│   ├── db.sqlite            # Structured product database
│
├── resources/
│   ├── faq_data.csv
│   └── ecommerce_chatbot_qna.csv
│
├── .env                     # Environment variables (not committed)
├── .gitignore
└── README.md
```

---

# ⚙️ Setup & Run Locally

## 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/E-commerce_chatbot.git
cd E-commerce_chatbot
```

---

## 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate:

Mac/Linux:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
GROQ_MODEL = llama-3.3-70b-versatile
GROQ_FAST = llama-3.3-70b-versatile

```

---

## 5️⃣ Run the Application

```bash
streamlit run app/main.py
```

---

# 🧪 Example Queries

```text
top rated mobiles under 20000
Nike shoes below 5000
what if the product is damaged
do you accept cash on delivery
who are you
```

---

# 🛡 Reliability & Guardrails

- Prevents hallucinated SQL columns via schema grounding  
- Handles LLM rate limits gracefully  
- Global exception handling to prevent crashes  
- Session-based memory to avoid cross-user leakage  
- Hybrid routing reduces misclassification errors  

---

# 📈 What I Learned

- Designing multi-capability LLM pipelines  
- Building hybrid routing systems (semantic + deterministic)  
- Preventing hallucination via retrieval grounding  
- Managing real-world constraints (rate limits, concurrency)  
- Structuring AI systems for production-readiness  

---

# 🎯 Why This Project Matters

Most chatbot demos rely purely on prompt engineering.

This project demonstrates:

- Structured data integration with LLMs  
- Controlled reasoning via schema-aware prompts  
- Retrieval grounding for factual reliability  
- Production-safe design considerations  

It reflects practical thinking in **LLM Engineering** and **AI System Architecture**.

---

# 🔮 Future Improvements

- Add product category metadata for better filtering  
- Introduce caching to reduce token usage  
- Add authentication & usage analytics  
- Deploy with containerization (Docker)  
- Add monitoring & logging dashboard  

---

# 🤝 Contributions & Feedback

Feedback, suggestions, and improvements are welcome.  

---

⭐ If you find this project interesting, consider giving it a star!

