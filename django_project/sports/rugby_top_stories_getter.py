import requests
from bs4 import BeautifulSoup

def main():
    url = "https://wwos.nine.com.au/rugby"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    x = soup.find("div", class_="feed__stories showVideoPlaceholder")
    print(x)



if __name__ == "__main__":
    main()
