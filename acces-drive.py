from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account
import os
import io

# Configurer les informations d'identification
SCOPES = ['https://drive.google.com/drive/folders/1h2JwpoilYqscgLAF8e01bhi46riXoc_Y?usp=sharing']
SERVICE_ACCOUNT_FILE = 'credentials.json'

def download_files_from_drive(folder_id, destination_folder):
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=creds)

    # Récupérer les fichiers dans le dossier Drive
    results = service.files().list(q=f"'{folder_id}' in parents",
                                   fields="files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('Aucun fichier trouvé.')
        return

    # Télécharger chaque fichier
    for item in items:
        file_id = item['id']
        file_name = item['name']
        request = service.files().get_media(fileId=file_id)
        fh = io.FileIO(os.path.join(destination_folder, file_name), 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f"Téléchargement {file_name}: {int(status.progress() * 100)}%")

# Exemple d'utilisation
download_files_from_drive('<ID_DU_DOSSIER_DRIVE>', 'documents/')
