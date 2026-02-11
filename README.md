🛍️ AI-Powered E-Commerce Chatbot

A production-style, multi-capability AI assistant that integrates LLM-powered Text-to-SQL, Retrieval-Augmented Generation (RAG), and Hybrid Intent Routing to handle real-world shopping queries reliably and safely.

This project goes beyond basic prompt engineering and demonstrates LLM system design, routing accuracy, grounding techniques, and production-aware AI architecture.

🔗 Live Demo & Repository

🔗 Live App: Add your deployed link here
🔗 GitHub Repository: Add your GitHub link here

🚀 Engineering Highlights

✅ Hybrid semantic + rule-based intent routing

✅ Schema-aware LLM Text-to-SQL pipeline

✅ Retrieval-Augmented FAQ system (hallucination-safe)

✅ Session-isolated conversational memory (multi-user safe)

✅ Defensive error handling for rate limits & API failures

✅ Production-aware architecture with modular design

🔍 Core Capabilities
📊 1️⃣ Product Search (LLM Text-to-SQL)

Users can query naturally:

“Top rated mobiles under 20000”
“Nike shoes below 5000”

How it works:

Natural language → LLM-generated SQL

Schema-aware prompt prevents hallucinated columns

Query executes over SQLite

Structured LLM response formatting

Supports:

Price range filters

Brand filters

Ratings

Popularity (total ratings)

Combined constraints

📚 2️⃣ FAQ & Policy Handling (RAG)

Handles support-related queries like:

“What if the product is damaged?”
“Do you accept cash on delivery?”

Architecture:

Sentence-transformer embeddings

Vector search via ChromaDB

Context-grounded LLM response

No answers outside retrieved data

Prevents hallucination by restricting responses strictly to retrieved context.

💬 3️⃣ General Conversational Queries

Handles:

“Who are you?”

“What can you do?”

Clarifications

Vague user inputs

Uses instruction-tuned LLMs with safe fallback logic.

🧠 System Architecture
User Query
   ↓
Hybrid Intent Router (Semantic + Rule-Based Guards)
   ↓
┌──────────────────────────────────────┐
│ Product Query                       │
│  → LLM Text-to-SQL                  │
│  → SQLite Execution                 │
│  → Structured LLM Response          │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│ FAQ / Policy Query (RAG)            │
│  → Embedding Generation             │
│  → ChromaDB Vector Search           │
│  → Context-Grounded LLM Response    │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│ General Conversation / Fallback     │
│  → Instruction-Tuned LLM            │
└──────────────────────────────────────┘

🛠️ Tech Stack

Language: Python
Frontend: Streamlit
Database: SQLite
LLMs: Groq-hosted LLaMA models
Intent Routing: Semantic Router
Vector Store: ChromaDB
Embeddings: Sentence Transformers
Environment Management: dotenv
Data Processing: Pandas

📂 Project Structure
E-commerce_chatbot/
│
├── app/
│   ├── main.py              # Streamlit app & routing orchestration
│   ├── router.py            # Semantic intent classification
│   ├── sql.py               # LLM Text-to-SQL pipeline
│   ├── faq.py               # RAG-based FAQ system
│   ├── general_qa.py        # Conversational QA
│   ├── fallback_qa.py       # Safe fallback handling
│   ├── db.sqlite            # Product database
│
├── resources/
│   ├── faq_data.csv
│   └── ecommerce_chatbot_qna.csv
│
├── .env                     # Environment configuration
├── .gitignore
└── README.md

⚙️ Setup & Run Locally
1️⃣ Clone Repository
git clone https://github.com/<your-username>/E-commerce_chatbot.git
cd E-commerce_chatbot

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv


Mac/Linux:

source venv/bin/activate


Windows:

venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file:

GROQ_API_KEY=your_api_key_here
SQL_MODEL=llama-3.3-70b-versatile
FAQ_MODEL=meta-llama/llama-3-8b-instruct
GENERAL_QA_MODEL=meta-llama/llama-3-8b-instruct
FALLBACK_MODEL=meta-llama/llama-3-8b-instruct

5️⃣ Run the Application
streamlit run app/main.py

🧪 Example Queries to Try

top rated mobiles under 20000

Nike shoes below 5000

what if the product is damaged

do you accept cash on delivery

who are you

🛡️ Production-Safe Design

The system includes:

Graceful handling of LLM rate limits (429 errors)

Exception-safe routing logic

No cross-user memory leakage

Session-isolated state management

Defensive fallback responses

The application never crashes or exposes stack traces to users.

📈 What I Learned

Designing multi-capability LLM systems beyond simple prompt usage

Implementing hybrid routing to reduce misclassification

Preventing hallucination via retrieval grounding

Structuring Text-to-SQL prompts safely

Managing concurrency and session isolation

Handling real-world constraints like rate limits and API instability

🎯 Why This Project Matters

Most chatbot demos rely purely on open-ended LLM prompts.

This project demonstrates:

Structured data integration with LLM reasoning

Controlled generation using schema-aware prompts

Retrieval-grounded answers instead of blind generation

Production-aware AI system design

It reflects real-world LLM application engineering principles.

🔮 Future Improvements

Add explicit product category metadata

Introduce caching to reduce token usage

Add advanced filtering (discount %, rating thresholds)

Add authentication and user analytics

Deploy with scalable backend (FastAPI + cloud hosting)

🤝 Contributions & Feedback

Feedback, suggestions, and improvements are welcome.
Feel free to open an issue or submit a pull request.

⭐ If you find this project interesting, consider giving it a star!
