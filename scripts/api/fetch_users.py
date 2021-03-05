import requests\nresponse = requests.get('https://jsonplaceholder.typicode.com/users')\nprint(response.json())
