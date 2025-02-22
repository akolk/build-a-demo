import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_code_and_tests(jira_data):
    prompt = f"""
    Based on the following JIRA requirements, generate a Python program and corresponding unit tests:
    
    Title: {jira_data['title']}
    Description: {jira_data['description']}
    Acceptance Criteria: {jira_data['acceptance_criteria']}
    
    Provide the main Python program and a test file using pytest.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
