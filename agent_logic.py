def generate_dockerfile(app_type="python"):
    print(f"Agent is analyzing code for: {app_type}")
    
    # Ye agent khud se decision le raha hai
    docker_template = f"""
FROM {app_type}:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
    """
    
    with open("Dockerfile.generated", "w") as f:
        f.write(docker_template)
    
    print("SUCCESS: Agent has generated a custom Dockerfile for the legacy app!")

if __name__ == "__main__":
    generate_dockerfile()