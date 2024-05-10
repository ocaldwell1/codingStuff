import requests

url = "  https://api.github.com/repos/ocaldwell1/codingStuff/commits"
headers = {"Accept": "application/vnd.github.inertia-preview+json"}
r = requests.get(url, headers=headers)