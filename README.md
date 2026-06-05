# VectorDB — Build a Vector Database from Scratch in C++

A fully working **Vector Database** built from scratch in C++ featuring an interactive web UI. This project implements **HNSW**, **KD-Tree**, and **Brute Force** search architectures side-by-side, combined with a **Retrieval-Augmented Generation (RAG) pipeline** powered entirely by local LLMs via Ollama.

Built as an educational implementation to demonstrate how production-grade vector search engines like Pinecone, Weaviate, and Chroma handle high-dimensional spatial indexing under the hood.

## 🚀 Key Features

* **3 Search Architectures:** Compare exact Brute-Force baseline calculations, KD-Tree binary spatial partitioning, and high-performance HNSW (Hierarchical Navigable Small World) proximity graphs.
* **2D Semantic Visualization:** Real-time projection of high-dimensional vectors onto a 2D canvas via Principal Component Analysis (PCA) to visually observe cluster formations.
* **Local RAG Integration:** Upload raw text documents, compute 768-dimensional embeddings using `nomic-embed-text`, and stream contextually bounded answers via `llama3.2`.
* **Full REST API Backend:** Powered by a clean, lightweight C++ single-header backend (`cpp-httplib`) running asynchronously via native OS threads.

## ⚙️ Tech Stack

* **Backend:** C++ (C++17)
* **Networking:** `cpp-httplib` (HTTP REST API & WebSockets)
* **AI Processing:** Ollama Engine (`llama3.2`, `nomic-embed-text`)
* **Frontend Dashboard:** HTML5, Vanilla JavaScript, CSS3 Canvas API

## 🔨 Setup & Run Execution

1. Make sure your local **Ollama** application is running in the background.
2. Compile the database engine with network socket linking flags:
   ```bash
   g++ -std=c++17 -O2 main.cpp -o db -lws2_32
