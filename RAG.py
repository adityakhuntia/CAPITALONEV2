# RAG.py — Lightweight MLX Model + FAISS RAG on Apple M2

import time
from mlx_lm import load as mlx_load, generate as mlx_generate
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# ----------------------------
# 1) Load a SMALL model via MLX
# ----------------------------
print("Loading TinyLLaMA 1.1B Chat 4-bit model...")
model, tokenizer = mlx_load("mlx-community/nano-llama-370m-mlx")


def run_llm(prompt: str, max_tokens: int = 300) -> str:
    return mlx_generate(model, tokenizer, prompt, max_tokens=max_tokens).strip()

# ----------------------------
# 2) Load and split documents
# ----------------------------
print("Loading PDF documents...")
loader = DirectoryLoader("docs", glob="**/*.pdf", loader_cls=PyPDFLoader)
docs = loader.load()

print("Splitting documents into chunks...")
splitter = RecursiveCharacterTextSplitter(chunk_size=900, chunk_overlap=150)
chunks = splitter.split_documents(docs)

# ----------------------------
# 3) Lightweight embeddings
# ----------------------------
print("Loading lightweight embeddings model...")
emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# ----------------------------
# 4) Build FAISS vector store
# ----------------------------
print("Building FAISS index...")
vectorstore = FAISS.from_documents(chunks, emb)

# ----------------------------
# 5) RAG function
# ----------------------------
def rag_query(question: str, k: int = 5) -> str:
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    docs = retriever.get_relevant_documents(question)
    context = "\n\n".join([doc.page_content for doc in docs])
    prompt = (
        "You are a helpful assistant. Use the provided context to answer the question.\n"
        "If the answer is not in the context, say you don't know.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}\nAnswer:\n"
    )
    return run_llm(prompt)

# ----------------------------
# 6) Run test query
# ----------------------------
start_time = time.time()
response = rag_query("Is it a good time to sow maize in Goa?")
duration = time.time() - start_time

print("\n--- RAG Answer ---")
print(response)
print(f"\nQuery took {duration:.2f} seconds.")
