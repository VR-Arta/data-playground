import json

users = json.loads(open('users.json').read())
print(len(users))
