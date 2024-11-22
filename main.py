from src.google_drive_handler import download_files
from src.index_builder import build_index
from src.chatbot import ask_question

if __name__ == "__main__":
    # Télécharger les documents
    folder_id = "https://drive.google.com/drive/folders/1h2JwpoilYqscgLAF8e01bhi46riXoc_Y?usp=sharing"
    download_files(folder_id, "documents/")

    # Construire l'index
    build_index("documents/", "index/")

    # Interagir avec le chatbot
    while True:
        query = input("Posez votre question : ")
        if query.lower() in ["quit", "exit"]:
            break
        print(ask_question(query, "index/"))
