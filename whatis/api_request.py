import requests
import pprint


response = requests.get('http://127.0.0.1:8000/api/v0/vacancyes/vacancyes/')

pprint.pprint(response.json())

response = requests.get('http://127.0.0.1:8000/api/v0/articles/articles/')

pprint.pprint(response.json())