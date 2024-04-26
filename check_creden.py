import os

def check_credentials():
    cred_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    if cred_path:
        print(f"Credentials path: {cred_path}")
        try:
            with open(cred_path, 'r') as file:
                print("Credentials file is accessible.")
        except Exception as e:
            print(f"Failed to access credentials file: {e}")
    else:
        print("GOOGLE_APPLICATION_CREDENTIALS is not set.")

check_credentials()      