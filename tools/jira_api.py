import requests
import os

JIRA_API_URL = "https://your-jira-instance.atlassian.net/rest/api/3/issue/"
JIRA_AUTH = (os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN"))

def fetch_jira_issue(issue_id):
    response = requests.get(f"{JIRA_API_URL}{issue_id}", auth=JIRA_AUTH)
    if response.status_code == 200:
        data = response.json()
        return {
            "title": data["fields"]["summary"],
            "description": data["fields"]["description"],
            "acceptance_criteria": data["fields"]["customfield_12345"]
        }
    else:
        return {"error": "Failed to fetch issue"}
