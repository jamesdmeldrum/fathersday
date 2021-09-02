import requests
from bs4 import BeautifulSoup

def main():
    url = "https://wwos.nine.com.au/rugby"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    x = soup.find_all("div", class_="story-block story-block--non-hero non-hero--article")[0]
    title = x.find("h3").text
    link = "https:" + x.find("a").get("href")

    dict = {
        "Title": title,
        "Link": link
    }

    return dict



if __name__ == "__main__":
    main()
