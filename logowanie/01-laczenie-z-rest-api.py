import requests
from requests.api import post

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')


if (response.status_code!= requests.codes.ok):
    print("COS NIE TAK")

else:
    print(response.json())

requestBody = {
    'title' : 'Nasz tytul',
    'body' : 'tRESC POSTA',
    'userId' : 1
}

response = requests.post('https://jsonplaceholder.typicode.com/posts',json=requestBody)


if (response.status_code!= requests.codes.created):
    print("COS NIE TAK")

else:
    print(response.json())
