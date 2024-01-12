import requests
from model import context, prompt
import os

API_URL = "https://api-inference.huggingface.co/models/consciousAI/question-answering-roberta-base-s-v2"
headers = {"Authorization": os.getenv("API_KEY")}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": {
		"question": prompt,
		"context": context
	},
})
print(output)