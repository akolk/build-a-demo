#import requests
#import os

#JIRA_API_URL = "https://your-jira-instance.atlassian.net/rest/api/3/issue/"
#JIRA_AUTH = (os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN"))

from tools.issues_tracker import update_issue

def fetch_jira_issue(issue_id):
    try:
        response = requests.get(f"{JIRA_API_URL}{issue_id}", auth=JIRA_AUTH)
        if response.status_code == 200:
            data = response.json()
            update_issue(issue_id, "jira", "Fetching JIRA data... ✅")
            return {
                "title": data["fields"]["summary"],
                "description": data["fields"]["description"],
                "acceptance_criteria": data["fields"]["customfield_12345"]
            }
        else:
            update_issue(issue_id, "jira", "Error Fetching JIRA Data ❌", response.text)
            return None
    except Exception as e:
        update_issue(issue_id, "jira", "JIRA Fetch Error ❌", str(e))
        return None
