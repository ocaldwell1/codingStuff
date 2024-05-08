import requests

url = "https://api.github.com/repos/rsapkf/42/commits"
headers = {"Accept": "application/vnd.github.inertia-preview+json"}
r = requests.get(url, headers=headers)