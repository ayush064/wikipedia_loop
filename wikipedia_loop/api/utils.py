import requests
from bs4 import BeautifulSoup

def get_first_link(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        content_div = soup.find(id='mw-content-text')
        if content_div:
            for link in content_div.find_all('a', href=True):
                if link['href'].startswith('/wiki/'):
                    return 'https://en.wikipedia.org' + link['href']
    except Exception as e:
        print(f"Error fetching page: {e}")
    return None

def wikipedia_loop(start_url):
    visited = []
    url = start_url
    count = 0

    while url:
        visited.append(url)
        next_url = get_first_link(url)

        if next_url is None or next_url in visited:
            break

        if "/wiki/Philosophy" in next_url:
            visited.append(next_url)
            break

        url = next_url
        count += 1

    return count, visited