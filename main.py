import requests
import sys

def fetch_githubActivity (username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)

    events = response.json()

    for event in events:
        type = event['type']
        repo = event['repo']['name']

        print(f"Name: {type} | Repository: {repo}")

def main():
    if len(sys.argv) < 2:
        print("Error: Please provide a username.")
        print("Usage: githubactivity <username>")
        sys.exit(1) 
    username = sys.argv[1]
    fetch_githubActivity(username)

if __name__ == "__main__":
            main()
