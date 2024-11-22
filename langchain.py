from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Charger les documents
loader = DirectoryLoader('documents', glob="*.txt")  # Utilisez le format adapté (PDF, TXT, etc.)
documents = loader.load()

# Diviser les textes pour l'indexation
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

# Créer des embeddings et un index FAISS
embeddings = OpenAIEmbeddings()  # Configurez avec votre clé OpenAI
vectorstore = FAISS.from_documents(texts, embeddings)

# Sauvegarder l'index
vectorstore.save_local("faiss_index")
