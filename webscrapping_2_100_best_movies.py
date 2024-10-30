from pprint import pprint
import requests
from bs4 import BeautifulSoup

response = requests.get('https://stacker.com/stories/1587/100-best-movies-all-time')
data = response.text
soup = BeautifulSoup(data, 'html.parser')
h2_tags = soup.find_all('h2', class_="ct-slideshow__slide__text-container__caption")

div_tag = [tag.text.split('\n')[1] for tag in h2_tags]
div_tag.reverse()
div_tag.pop(100)
pprint(div_tag)