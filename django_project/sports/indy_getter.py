import requests
from bs4 import BeautifulSoup


def event_getter(soup):
    x = soup.find_all("li", class_="schedule-list__item")
    for a in x:
        text = a.find("div", class_="schedule-list__content").text
        text_lower = filter_shit_out(text)
        try:
            month = a.find("div", class_="schedule-list__date").text
            month = filter_shit_out(month)
            date = a.find("div", class_="schedule-list__date").find("span", class_="schedule-list__date-day").text
            date = filter_shit_out(date)
            date = int(date) + 1
            time = a.find("span", class_="timeEst").text
            time = time.split(":")
            hour = time[0]
            hour = int(hour) + 12 - 10
            time[0] = "0" + str(hour)
            time = ':'.join(time)

            dict = {
                "Title": text_lower,
                "Month": month,
                "Date": date,
                "Time": time[:-6]
            }

            return dict
        except Exception:
            pass




def main():
    url = "https://www.indycar.com/Schedule"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return event_getter(soup)#, news_getter(soup)


def filter_shit_out(text):
    text = list(text)
    new = []

    letters_numbers = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")

    add_to_list = False
    last_space = False
    for i in text:
        if i in letters_numbers:
            new.append(i)
            add_to_list = True
        else:
            if add_to_list == True:
                new.append(i)
                last_space = True
                add_to_list = False
            elif last_space == True:
                new.pop(len(new)-1)
                return ''.join(new)
    return ''.join(new)

if __name__ == "__main__":
    main()
