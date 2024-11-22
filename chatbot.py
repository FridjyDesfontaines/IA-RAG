import ollama
from langchain.vectorstores import FAISS

def ask_question(query, index_folder):
    vectorstore = FAISS.load_local(index_folder)
    docs = vectorstore.similarity_search(query, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])
    response = ollama.complete(
        prompt=f"Voici le contexte :\n{context}\n\nQuestion : {query}\nRéponse :",
        model="llama"
    )
    return response['response']
