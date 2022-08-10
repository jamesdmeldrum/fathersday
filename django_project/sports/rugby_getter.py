import requests
from bs4 import BeautifulSoup

def get_next_rugby(rugby_url):
    page = requests.get(rugby_url)
    soup = BeautifulSoup(page.content, "html.parser")

    x = soup.find_all("div", class_="games-list-item")

    for line in x:
        date = line.find("div", class_="date").text.strip()
        matches = line.find_all("div", class_="game")
        for match in matches:
            home_team = match.find("div", class_="team home").text.strip()
            away_team = match.find("div", class_="team away").text.strip()
            if home_team == "Australia" or away_team == "Australia":
                time = match.find("div", class_="game-time").text
                dict = {
                    "home_team": home_team,
                    "away_team": away_team,
                    "date": date,
                    "time": time
                }

                return dict



def format_rugby_details(details):
    details = details.split(" - ")
    location = details[0]
    date_time = details[1]
    date_time = date_time.split(", ")
    date = date_time[0]
    time = date_time[1].split(" ")[0]
    time = format_rugby_time(time)
    return [date, time]

def format_rugby_time(time):
    time = time.split(":")
    hour = time[0]
    min = time[1]
    hour = int(hour) + 10
    return str(hour) + ":" + min


def main():
    rugby_url = 'https://www.rugbypass.com/internationals/fixtures-results/'
    returned = get_next_rugby(rugby_url)

    print(returned)

    return returned

if __name__ == "__main__":
    main()
