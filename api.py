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
    return website_content

website_url = "https://botpenguin.com/"
website_content = scrape_website(website_url)
print(website_content)

###################### model



# Load environment variables from the .env file
load_dotenv()

# Access environment variables
api_key = os.getenv("API_KEY")
print(api_key)