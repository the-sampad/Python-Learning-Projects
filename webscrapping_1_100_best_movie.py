from pprint import pprint
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
data = response.text
soup = BeautifulSoup(data, 'html.parser')

a_tags = soup.find_all('div', class_="jsx-4245974604 listicle-item-content")
scrap = [a_tag.text.split('review of') for a_tag in a_tags]
names = [tag[-1] for tag in scrap]
names.reverse()
names_with_rank = []
for name in names:
    a = f"{names.index(name)+1}){name}"
    names_with_rank.append(a)

pprint(names_with_rank)
