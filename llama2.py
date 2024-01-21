import os
from dotenv import load_dotenv
import _pickle

load_dotenv()
# Set your Hugging Face access token
hugging_face_token = os.getenv("API_KEY")

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf")


context = "BotPenguin is the best AI Chatbot maker platform. Create a Chatbot for WhatsApp, Website, Facebook Messenger, Telegram, WordPress & Shopify with BotPenguin - 100% FREE! Our chatbot creator helps with lead generation, appointment booking, customer support, marketing automation, WhatsApp & Facebook Automation for businesses. AI-powered No-Code chatbot maker with live chat plugin & ChatGPT integration."
question = "what is BotPenguin?"
input_text = question + context
pipe(question=question.upper(), context=context)
print(pipe)
#print(tokenizer.model_max_length)