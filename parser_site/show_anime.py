import requests
from bs4 import BeautifulSoup


URL = "https://animevost.am/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="shortstoryContent")

    anime = []

    for item in items:
        anime.append(
            {
                "title": item.find('a').get("href"),
                "image": URL + item.find(class_="imgRadius").get("src"),
            }
        )
    print(anime)
    return anime


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        anime = []
        for page in range(1):
            html = get_html(f"https://animevost.am/page/{page}/")
            anime.extend(get_data(html.text))
        return anime
    else:
        raise Exception("Error in parser function")




