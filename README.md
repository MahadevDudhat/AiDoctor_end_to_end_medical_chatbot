# 🩺 Aidoctor – AI-Powered Medical Chatbot

Aidoctor is a conversational AI chatbot designed to answer medical queries by referencing a structured knowledge base built from a medical PDF. It leverages state-of-the-art technologies including LangChain, Pinecone, and Google's Gemini API to deliver contextual and relevant responses based on authoritative content.

---

## 🚀 Features

- 📘 PDF chunking and embedding of medical textbook
- 🧠 Vector storage and retrieval via Pinecone
- 🤖 Natural language interaction powered by Gemini API
- 🔗 LangChain for chaining and orchestration
- 🌐 REST API powered by Flask

---

## 🛠️ Tech Stack

| Tool         | Purpose                                    |
|--------------|---------------------------------------------|
| Python       | Core development language                   |
| Flask        | API backend                                 |
| LangChain    | Prompt orchestration and chaining logic     |
| Pinecone     | Vector database for semantic search         |
| Gemini API   | LLM interface for intelligent responses     |

---

## 📂 Project Workflow

1. **PDF Chunking**: Large medical book split into manageable chunks.
2. **Embedding**: Each chunk transformed into vector format using LangChain.
3. **Vector Storage**: Embedded chunks stored in Pinecone.
4. **User Query Handling**: Flask routes incoming questions.
5. **Vector Retrieval**: Relevant chunks retrieved via semantic similarity.
6. **Answer Generation**: Gemini API generates responses based on query + retrieved context.

