# Generative AI & RAG Exploration

This repository contains code, experiments, and Jupyter Notebooks focused on building Generative AI applications and Retrieval-Augmented Generation (RAG) pipelines. It utilizes modern AI frameworks, primarily LangChain, to process documents, generate embeddings, and interact with Large Language Models (LLMs).

## 🗂️ Project Structure

The repository is organized into sequential modules that follow a standard RAG pipeline:

* **`01_document_loaders/`**: Techniques for ingesting raw data (PDFs, Webpages, text files) into actionable Document objects.
* **`02_text_splitters/`**: Implementation of various chunking strategies (e.g., `RecursiveCharacterTextSplitter`, `HTMLHeaderTextSplitter`) to prepare documents for embedding while preserving semantic context.
* **`03_embeddings/`**: Converting text chunks into vector representations using embedding models (e.g., OpenAI) and storing them in vector databases.
* *(More modules will be added as the project expands)*

## 🛠️ Tech Stack & Tools
* **Language:** Python
* **Framework:** LangChain
* **Environment:** Jupyter Notebooks
* **Observability:** LangSmith

## 🚀 Getting Started

Follow these steps to set up the project on your local machine.

### 1. Clone the repository
```powershell
git clone [https://github.com/abhishekjha462000/Generative_AI.git](https://github.com/abhishekjha462000/Generative_AI.git)
cd Generative_AI