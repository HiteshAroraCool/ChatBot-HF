import contextlib
import requests
from bs4 import BeautifulSoup
import _pickle

def links(website_html: str) -> list[str]:
    soup = BeautifulSoup(website_html, 'html.parser')
    return [link.get('href') for link in soup.find_all('a')]

def scrape_website(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Error making request to {url}: {e}")
        return None

    if response.status_code != 200:
        print(f"Error: non-200 status code received from {url}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    website_html = soup.prettify()
    links_list = links(website_html)
    print(links_list)
    website_content = soup.get_text().strip()
    return website_content

website_url = "https://botpenguin.com/"
feature = scrape_website(website_url)
label = "Home page"




if feature is not None and label is not None:
    with contextlib.ExitStack() as stack:
        file = stack.enter_context(open('data.pkl', 'wb'))
        _pickle.dump((feature, label), file)