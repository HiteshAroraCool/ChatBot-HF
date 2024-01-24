from gensim.parsing.preprocessing import remove_stopwords
import requests
from bs4 import BeautifulSoup
import _pickle
import re

def clean_webpage_content(webpage_content):
    # Remove JavaScript code
    webpage_content = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', webpage_content, flags=re.DOTALL)

    # Remove HTML tags
    webpage_content = re.sub(r'<[^>]+>', '', webpage_content)

    # Remove unnecessary text
    unwanted_phrases = [
        r'.*?Claim close',
        r'Integrations arrow_right_alt.*?Key Features arrow_right_alt',
        r'ComparisonsBotPenguin Vs.*?LandbotProduct What do\?Who use it\?Where run\?',
        r'Pricing Chatbot Pricing \(except WA\) arrow_right_alt.*?Website, Telegram, Facebook Live Chat bots',
        r'Partners Partners Home arrow_right_alt.*?Earn clients happierImplementation Partners arrow_right_alt',
        r'expand_more Integrations arrow_right_alt.*?expand_more DO MORE Chat Automation!',
        re.escape(r'arrow_right_alt'),  # Escape individual characters
        re.escape(r'Enter Name*Enter Email*+ expand_more Enter Phone NumberEnter Facebook Page Link*10k 100k100k 1Mn1Mn 3Mn3Mn 10Mn10Mn+ Select number followers*Less 100k100k 500k500k+ Select number FB messages get*Enter informationCancelClaimBy submitting form agree terms. View privacy policy learn use information.'),
    ]
    for phrase in unwanted_phrases:
        webpage_content = re.sub(phrase, '', webpage_content, flags=re.DOTALL)

    # Remove extra whitespaces
    webpage_content = ' '.join(webpage_content.split())

    return webpage_content

def links(website_html: str) -> list[str]:
    soup = BeautifulSoup(website_html, 'html.parser')
    return {link.get('href').replace("/", ""): 'https://botpenguin.com' + link.get('href') for link in soup.find_all('a')}

def scrape_and_store(url, label):
    print(f"Scraping {label} ({url})")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error making request to {url}: {e}")
        return None

    if response.status_code != 200:
        print(f"Error: non-200 status code received from {url}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    website_html = soup.prettify()
    links_list = links(website_html)
    print(f"Links Found on {label}: {len(links_list)}")
    website_content = remove_stopwords(soup.get_text())

    return website_content, links_list


if __name__=='__main__':
    
    website_urls = {"Home page": "https://botpenguin.com/"}

    # Save the website text content and links in a pickled file if the file does not exist, it will create one.
    # More idea: we can use the link list to scrape other pages, make sure to append to pkl instead of replacing existing data.
    for label, url in website_urls.items():
        website_content, links_list = scrape_and_store(url, label)
        cleaned_content = clean_webpage_content(website_content)
        print(cleaned_content)

        if cleaned_content is not None and label is not None:
            data = {'label': label, 'context': cleaned_content, 'links': links_list}
            with open('data.pkl', 'wb') as file:
                _pickle.dump(data, file)
            print(f"{label} data extracted")