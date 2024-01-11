import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

def scrape_website(url):
    respone = requests.get(website_url, timeout=10)
    soup = BeautifulSoup(respone.text, 'html.parser')
    #print("This is the text extacted:", soup.get_text())
    website_html = soup.prettify()
    website_content = soup.get_text()
    return website_content.strip()

website_url = "https://botpenguin.com/"
website_content = scrape_website(website_url)
#print(website_content)


###################### model

# Load environment variables from the .env file
load_dotenv()
# Access environment variables
api_key = os.getenv("API_KEY")


from transformers import GPT2LMHeadModel, GPT2Tokenizer

model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

prompt = "what is BotPenguin?" 
context = "BotPenguin is the best AI Chatbot maker platform. Create a Chatbot for WhatsApp, Website, Facebook Messenger, Telegram, WordPress & Shopify with BotPenguin - 100% FREE! Our chatbot creator helps with lead generation, appointment booking, customer support, marketing automation, WhatsApp & Facebook Automation for businesses. AI-powered No-Code chatbot maker with live chat plugin & ChatGPT integration."
input_text = prompt + "\n" + context
input_ids = tokenizer.encode(input_text, return_tensors="pt")
output = model.generate(input_ids, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)
response = tokenizer.decode(output[0], skip_special_tokens=True)
print(response)