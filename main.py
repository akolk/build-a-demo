from crewai import Agent, Task, Crew
from tools.jira_api import fetch_jira_issue
from tools.github_api import create_github_repo, push_code
from tools.llm_codegen import generate_code_and_tests
from tools.deployment import create_dockerfile, deploy_application


issue_id = "JIRA-12345"  # Example issue ID
issue_source = "github"  # Change to "github" if using GitHub Issues

# JIRA Agent
jira_agent = Agent(
    name="JIRA Agent",
    role="Fetches user story from JIRA",
    function=lambda: fetch_jira_issue(issue_id)
)

# Code Generation Agent
code_gen_agent = Agent(
    name="Code Generation Agent",
    role="Generates Python code and tests",
    function=lambda: generate_code_and_tests(fetch_jira_issue(issue_id), issue_source)
)

# GitHub Agent
github_agent = Agent(
    name="GitHub Agent",
    role="Creates a repository and pushes code",
    function=lambda: create_github_repo("repo-name", issue_id, issue_source)
)

# Deployment Agent
deployment_agent = Agent(
    name="Deployment Agent",
    role="Generates a Dockerfile and deploys the app",
    function=lambda: deploy_application(issue_id, issue_source)
)

# Define Tasks
task1 = Task(agent=jira_agent, description="Fetch user story from JIRA")
task2 = Task(agent=code_gen_agent, description="Generate Python code and tests")
task3 = Task(agent=github_agent, description="Create GitHub repo and push code")
task4 = Task(agent=deployment_agent, description="Generate Dockerfile & deploy")

# Assemble Crew
crew = Crew(agents=[jira_agent, code_gen_agent, github_agent, deployment_agent])
crew.run([task1, task2, task3, task4])
