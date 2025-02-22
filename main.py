from tools.github_api import get_open_issues, create_github_repo, update_github_issue
from tools.llm_codegen import generate_code
from tools.deployment import generate_dockerfile_and_deploy

# Fetch open GitHub issues
issues = get_open_issues()

for issue in issues:
    issue_id = issue["number"]
    issue_title = issue["title"]
    issue_body = issue["body"]
    repo_name = f"demo-{issue_id}"  # Generate a unique repo name

    update_github_issue(issue_id, "Processing started... ⚙️")

    # Step 1: Create GitHub Repo
    repo = create_github_repo(repo_name, issue_id)
    if not repo:
        continue  # Skip to next issue if repo creation fails

    # Step 2: Generate Code
    code = generate_code(issue_title, issue_body, issue_id)
    if not code:
        continue  # Skip to next issue if code generation fails

    # Step 3: Push Code to GitHub (mocked)
    update_github_issue(issue_id, "Pushing Code to GitHub... ⏳")
    # Here you would add logic to push the generated code
    update_github_issue(issue_id, "Code Pushed Successfully ✅")

    # Step 4: Generate Dockerfile & Deploy
    generate_dockerfile_and_deploy(issue_id)

    update_github_issue(issue_id, "Processing completed! 🎉")
