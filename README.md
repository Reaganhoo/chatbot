#📄 Policy Chatbot using RAG (LangChain + Gemini + ChromaDB)

This project is a Retrieval-Augmented Generation (RAG) chatbot that answers questions based on a company policy PDF instead of relying on an LLM’s internal knowledge.

It uses Google Gemini, LangChain, and ChromaDB to perform semantic search and generate accurate, grounded responses.

🎓 Built using Gemini’s free student tier, making it accessible for learners.

---
##🚀 Features
- 📚 Ask questions directly from a PDF knowledge base
- 🔍 Semantic & similarity search using embeddings
- 🧠 RAG architecture (Retrieval → Augmentation → Generation)
- 💾 Persistent vector database
- 💬 Web-based chat UI using Gradio

---
##🧱 Project Structure
```bash
.
├── chroma_langchain_db/   # ChromaDB persistent vector database
├── company_policy.pdf    # Knowledge base (source document)
├── demo.png              # Screenshot of chatbot demo
├── main.py               # Main application code
├── requirements.txt      # Required Python libraries
└── README.md
```
---
##🧠How It Works (RAG Pipeline)
1. Document Ingestion
 - Load company_policy.pdf
 - Split text into small overlapping chunks
 - Convert text into embeddings using gemini-embedding-001

2. Vector Storage
 - Store embeddings in ChromaDB
 - Persist data locally for reuse

3. Retrieval
 - Perform semantic similarity search
 - Retrieve the most relevant chunk (top k = 1)

4. Prompt Engineering
 - Combine retrieved context + user question
 - Ground the model with system instructions to prevent hallucination

5. Response Generation
 - Gemini generates answers only from retrieved context

6. User Interface
 - Gradio ChatInterface for real-time interaction
---
##🖼️ Demo
Below is an example of the chatbot answering questions based on the company policy:
<img width="1204" height="431" alt="demo" src="https://github.com/user-attachments/assets/35ca041a-1816-49e9-8c8f-84c49b23795f" />
---
##⚙️ Installation & Setup
1️⃣ Clone the repository
```bash
git clone https://github.com/Reaganhoo/chatbot.git
cd chatbot
```
2️⃣Install dependencies
```bash
pip install -r requirements.txt
```
---
##Key Learnings from This Project
- Difference between RAG vs fine-tuning
- Semantic search vs keyword search
- Prompt grounding to reduce hallucination
- Importance of architecture in AI systems
---
##🧠 Tech Stack
- Python
- LangChain
- Google Gemini (LLM + Embeddings)
- ChromaDB
- Gradio
---
##🙌 Acknowledgements
- Google Gemini (Student Free Tier)
- LangChain community
- ChromaDB
- Gradio
