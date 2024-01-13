import requests
import os
from dotenv import load_dotenv
from transformers import pipeline
import _pickle

load_dotenv()

question = "what is BotPenguin?"

with open("data.pkl", "rb") as f:
    context, label = _pickle.load(f)


API_URL = "https://api-inference.huggingface.co/models/consciousAI/question-answering-roberta-base-s-v2"
API_URL = "https://api-inference.huggingface.co/models/Andron00e/YetAnother_Open-Llama-3B-LoRA-OpenOrca"
headers = {"Authorization": os.getenv("API_KEY")}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": {
		"question": question,
		"context": context
	},
})
print(output)