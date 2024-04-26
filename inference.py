
import requests

API_URL = "https://api-inference.huggingface.co/models/dslim/bert-base-NER"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
