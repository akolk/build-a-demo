import requests
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_ORG = "your-org-name"

def create_github_repo(repo_name):
    url = f"https://api.github.com/orgs/{GITHUB_ORG}/repos"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    data = {"name": repo_name, "private": False}
    
    response = requests.post(url, json=data, headers=headers)
    return response.json()

def push_code(repo_name, files):
    repo_url = f"https://api.github.com/repos/{GITHUB_ORG}/{repo_name}/contents/"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    for file_name, content in files.items():
        data = {"message": f"Add {file_name}", "content": content.encode("utf-8")}
        requests.put(repo_url + file_name, json=data, headers=headers)
