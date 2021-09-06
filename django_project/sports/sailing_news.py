import requests
from bs4 import BeautifulSoup


def main():
    url = "https://sailgp.com/news/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    x = soup.find_all("div", class_= "c-full-hub__grid-item")

    for a in x:
        title = a.find("div", class_="c-content-card__heading").text
        print(title)
        dict = {
            "Title": title,
            "Link": url
        }
        return dict

if __name__ == "__main__":
    main()
