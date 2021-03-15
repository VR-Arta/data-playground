import json\nusers = json.loads(open('users.json').read())\nprint(len(users))
