import requests
from bs4 import BeautifulSoup



def main():
    url = "https://au.motorsport.com/v8supercars/news"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    x = soup.find_all("div", class_="ms-item--art")
    top = x[0].find_all("a")[0]
    link = url + top.get("href")
    title = top.get("title")

    dict = {
        "Title": title,
        "Link": link
    }

    return dict


if __name__ == "__main__":
    main()
