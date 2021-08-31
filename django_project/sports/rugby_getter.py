import requests
from bs4 import BeautifulSoup

def get_next_rugby(rugby_url):
    page = requests.get(rugby_url)
    soup = BeautifulSoup(page.content, "html.parser")

    x = soup.find_all("li", class_="single-fixture single-fixture--scheduled home-away-match")

    for line in x:
        home_element = line.find("div", class_="team team--home")
        home_team = home_element.find("div", class_="team__name fixture__team-name").text
        away_element = line.find("div", class_="team team--away")
        away_team = away_element.find("div", class_="team__name fixture__team-name").text

        if home_team == "Australia" or away_team == "Australia":
            details = line.find("div", class_="fixture__venue-time")
            details = format_rugby_details(details.text)

            print(home_team)
            print(away_team)
            print(details[0], details[1])

            dict = {
                "home_team": home_team,
                "away_team": away_team,
                "date": details[0],
                "time": details[1]
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
    rugby_url = 'https://wwos.nine.com.au/rugby/live-scores/fixtures'
    return get_next_rugby(rugby_url)

if __name__ == "__main__":
    main()
