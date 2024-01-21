from gensim.parsing.preprocessing import remove_stopwords
import requests
from bs4 import BeautifulSoup
import _pickle

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

        if website_content is not None and label is not None:
            data = {'label': label, 'context': website_content, 'links': links_list}
            with open('data.pkl', 'wb') as file:
                _pickle.dump(data, file)
            print(f"{label} data extracted")
    