import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_next_cars(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    x = soup.find_all("div", class_="event-item")
    today = datetime.now()
    for a in x:
        date = a.find("div", class_="event-item-date")
        title = a.find("a", class_="event-item-title")
        date = correct_output(date.text)
        dt = get_dt(date)
        diff = (dt - today).total_seconds()
        if diff > 0:
            title = correct_output(title.text)
            title = correct_title(title)
            month = ''.join(list(date)[0:3])
            dates = ''.join(list(date)[3:])
            month = match_month(month)

            dict = {
                "Event": title,
                "Month": month,
                "Dates": dates
            }
            return dict

def correct_title(title):
    title = list(title)

    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowers = capitals.lower()
    capitals = list(capitals)
    lowers = list(lowers)
    numbers = list("0123456789")

    output = ''
    counter = 0
    number = False
    for elem in title:
        if elem in lowers or counter == 0:
            number = False
            output += elem
            counter += 1
        elif elem in numbers:
            if number:
                output += elem
            else:
                output = output + ' ' + elem
                number = True
        else:
            number = False
            output = output + ' ' + elem

    return output



def match_month(month):
    full_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    short_months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

    if month not in full_months:
        for i in range(12):
            if month.lower() == short_months[i].lower():
                month = full_months[i+1]
                return month

def get_dt(date):
    month = ''.join(list(date)[0:3])
    start = ''.join(list(date)[3:5])
    end = ''.join(list(date)[6:])
    month = get_month_int(month)
    year = datetime.today().year
    event_datetime = datetime(year, month, int(end))
    return event_datetime

def get_month_int(month):
    short_months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    for i in range(1,13):
        if month.lower() == short_months[i]:
            return i

def correct_output(input):
    input = list(input)
    allowed = list("abcdefghijklmnopqrstuvwxyz0123456789-")
    output = []
    for elem in input:
        if elem.lower() in allowed:
            output.append(elem)
    return ''.join(output)


def main():
    url = 'https://www.supercars.com/calendar/'
    return get_next_cars(url)

if __name__ == "__main__":
    main()
