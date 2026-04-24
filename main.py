import requests

userName = "goncalvespedroo"
url = f"https://api.github.com/users/{userName}/events"
response = requests.get(url)

events = response.json()

for event in events:
    type = event['type']
    repo = event['repo']['name']

    print(f"Name: {type} | Repository: {repo}")
