import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import os
from dotenv import load_dotenv

load_dotenv()

FIREBASE_CREDENTIAL_PATH = os.getenv('FIREBASE_CREDENTIAL_PATH')

# Initialize Firebase Admin SDK
def initialize_firebase():
    cred = credentials.Certificate(FIREBASE_CREDENTIAL_PATH)
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'bubbleupload-a8c67.appspot.com'
    })

# Function to upload a file to Firebase Storage and get the download URL
def upload_file_to_firebase(file_path):
    # Ensure Firebase is initialized
    if not firebase_admin._apps:
        initialize_firebase()
        

    # Get the bucket
    bucket = storage.bucket()

    # Upload the file
    blob = bucket.blob(file_path)
    with open(file_path, "rb") as doc_file:
        blob.upload_from_file(doc_file)

    # Make the blob publicly accessible
    blob.make_public()

    # Get the public URL
    return blob.public_url

# Example usage
# if __name__ == "__main__":
#     file_path = 'path_to_your_docx_file.docx'
# download_url = upload_file_to_firebase("C:\\Users\\Dell\\OCR_NER\\tanu\\singh\\saved_docx\\OutputText.docx")
# print("Download URL:", download_url)
