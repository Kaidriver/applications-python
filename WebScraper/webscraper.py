#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup

URL = "https://www.foxsports.com/nfl/scores"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
quotes=[]  # a list to store quotes

team_name = input("Enter team name: ")

team = soup.find('span', text=team_name) 
parentWrapper = team.parent.parent

team_abbreviation = parentWrapper.find('div', class_='score-team-name abbreviation').find('span').text

if parentWrapper.find('div', class_='score-team-score'):
    print(team_name + " " + parentWrapper.find('div', class_='score-team-score').find('span', class_='scores-text').text.strip())
else:
    print(team_name)

other_team = parentWrapper.parent.find('span', class_='scores-text', text=lambda x: x != team_name and x != team_abbreviation)
other_team_wrapper = other_team.parent.parent
if other_team_wrapper.find('div', class_='score-team-score'):
    print(other_team.text + " " + other_team_wrapper.find('div', class_='score-team-score').find('span', class_='scores-text').text.strip())
else:
    print(other_team.text)
