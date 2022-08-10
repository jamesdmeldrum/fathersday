import requests
from bs4 import BeautifulSoup

def get_next_cricket(cricket_url, printit = False):
    page = requests.get(cricket_url)
    soup = BeautifulSoup(page.content, "html.parser")

    x = soup.find_all("div", class_="ds-border-b ds-border-line ds-border-r ds-w-1/2")

    if printit == True:
        print(x)

    for a in x:
        time = a.find("div", class_="ds-truncate ds-w-[90%]")
        date_time = time.text

        date = date_time.split(", ")[0:2]
        date = format_cricket_date(date)
        try:
            time = date_time.split(", ")[2]
            time = format_cricket_time(time)
        except:
            time = ""

        teams = a.find("div", class_="ds-flex ds-flex-col ds-mt-2 ds-mb-2")
        team_1 = teams.find_all("p", class_="ds-text-tight-m ds-font-bold ds-capitalize")[0].text
        team_2 = teams.find_all("p", class_="ds-text-tight-m ds-font-bold ds-capitalize")[1].text

        dict = {
            "home_team": team_1,
            "away_team": team_2,
            "date": date,
            "time": time
        }



        return dict

def format_cricket_time(time):
    time = time.split(" ")[0]
    hour = int(time.split(":")[0])
    diff = 11
    hour = hour + diff
    return str(hour) + ":" + time.split(":")[1]

def format_cricket_date(date):
    full_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    short_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    full_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    short_months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

    if date[0] not in full_days:
        for i in range(7):
            if date[0].lower() == short_days[i].lower():
                date[0] = full_days[i]
                break

    month = date[1].split(" ")[1]
    if month not in full_months:
        for i in range(12):
            if month.lower() == short_months[i].lower():
                month = full_months[i]
                break

    dat_num = date[1].split(" ")[0]
    th = "th"
    if list(dat_num)[1] == "1":
        th = "st"
    elif list(dat_num)[1] == "2":
        th = "nd"
    elif list(dat_num)[1] == "3":
        th = "rd"

    dat_num = dat_num + th

    return date[0] + " " + month + " " + dat_num

def main(printit=False):
    cricket_url = "https://www.espncricinfo.com/team/australia-2/match-schedule-fixtures"
    returned = get_next_cricket(cricket_url, printit = True)

    if printit == True:
        print(returned)

    return returned


if __name__ == "__main__":
    main(printit = True)
