import requests
from bs4 import BeautifulSoup
from datetime import datetime, date

def next_event():
    url = "https://sailgp.com/about/2021/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    x = soup.find_all("div", class_="c-calendar__list-item")
    for a in x:
        dates = a.find("div", class_="c-calendar-card__dates").text
        start_date = dates.split(" - ")[0]
        end_date = dates.split(" - ")[1].split(" ")[0]
        month = dates.split(" - ")[1].split(" ")[1]
        year = int(dates.split(" - ")[1].split(" ")[2])
        month_int = month_to_int(month)

        date_time = datetime(year, month_int, int(end_date))
        today = datetime.now()

        if (today - date_time).total_seconds() < 0:
            event_name = a.find("span", class_="c-calendar-card__location").text
            date = format_date(start_date, end_date, month, str(year))

            dict = {
                "Name": event_name,
                "Date": date
            }


            return dict

def format_date(start_date, end_date, month, year):
    str = start_date + ' - ' + end_date + ' ' + month + ', ' + year
    return str


def month_to_int(month):
    short_months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(" ")
    for i in range(1,13):
        if month.lower() == short_months[i-1].lower():
            return i

def main():
    return next_event()

if __name__ == "__main__":
    main()
