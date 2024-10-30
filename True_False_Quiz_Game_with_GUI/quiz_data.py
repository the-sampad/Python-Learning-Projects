import requests

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean")
response.raise_for_status()
data = response.json()
ques_data = data['results']