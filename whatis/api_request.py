import requests
import pprint


response = requests.get('http://127.0.0.1:8000/api/v0/vacancyes/vacancyes/', auth=('udo', 'ntcnbhjdfybt1'))

pprint.pprint(response.json())

response = requests.get('http://127.0.0.1:8000/api/v0/articles/articles/', auth=('user1', 'ntcnbhjdfybt1'))

pprint.pprint(response.json())

response = requests.get('http://127.0.0.1:8000/api/v0/articles/articles/', auth=('user0', ''))

response = requests.get('http://127.0.0.1:8000/api/v0/articles/articles/')

pprint.pprint(response.json())


response = requests.get('http://127.0.0.1:8000/api/v0/articles/skills/', auth=('user2', 'ntcnbhjdfybt2'))
pprint.pprint(response.json())

response = requests.get('http://127.0.0.1:8000/api/v0/articles/skills/', auth=('user2', 'ntcnbhjdfybt'))
pprint.pprint(response.json())

response = requests.get('http://127.0.0.1:8000/api/v0/articles/skills/')
pprint.pprint(response.json())


token = 'bc9cd4b93ed55c04801b172fbba8e4cb9232c470'
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/v0/skills/', headers=headers)
# response = requests.get('http://127.0.0.1:8000/api/v0/tags/')
pprint.pprint(response.json())

token = 'cc9cd4b93ed55c04801b172fbba8e4cb9232c470'
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/v0/skills/', headers=headers)
# response = requests.get('http://127.0.0.1:8000/api/v0/tags/')
pprint.pprint(response.json())