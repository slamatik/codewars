from bs4 import BeautifulSoup
import urllib.request

URL = 'https://www.codewars.com/users/leaderboard'


class User:
    def __init__(self, name, clan, honor):
        self.name = name
        self.clan = clan
        self.honor = honor


class Leaderboard:
    def __init__(self, list_of_users):
        position = {}
        for pos, user in enumerate(list_of_users, 1):
            position[pos] = user
        self.position = position


def solution():
    source = urllib.request.urlopen(URL).read()
    soup = BeautifulSoup(source, 'html.parser')
    table = soup.find('table')
    table_rows = table.find_all('tr')
    list_of_users = []
    for tr in range(1, len(table_rows)):
        td = table_rows[tr].find_all('td')
        row = [i.text for i in td]
        name = row[1][5:]
        clan = row[2]
        honor = int(row[-1].replace(",", ""))
        user = User(name, clan, honor)
        list_of_users.append(user)

    leaderboard = Leaderboard(list_of_users)
    return leaderboard


leaderboard = solution()
for i in range(1, 6):
    an_alien = leaderboard.position[i]
    print(an_alien.name, an_alien.clan, an_alien.honor)
