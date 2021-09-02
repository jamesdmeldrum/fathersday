import requests
from bs4 import BeautifulSoup





def main():
    url = "http://cricket.com.au"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    x = soup.find_all("h2")[0]
    story_title = x.text
    story_link = "https://cricket.com.au" + x.find("a").get('href')

    dict = {
        "Title": story_title,
        "Link": story_link
    }

    return dict

if __name__ == "__main__":
    main()
