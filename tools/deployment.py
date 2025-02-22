def create_dockerfile():
    dockerfile_content = """
    FROM python:3.9
    WORKDIR /app
    COPY requirements.txt .
    RUN pip install -r requirements.txt
    COPY . .
    CMD ["python", "main.py"]
    """
    return dockerfile_content

def deploy_application():
    print("🚀 Deploying the application using GitHub Actions...")
