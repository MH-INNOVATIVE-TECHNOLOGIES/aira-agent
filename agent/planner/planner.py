class Planner:
    def __init__(self):
        pass

    def create_plan(self, analysis: dict):
        plan = {
            "steps": [],
            "dockerfile": "",
            "deployment": []
        }

        tech_stack = analysis.get("tech_stack", [])
        issues = analysis.get("issues", [])

        # 🔹 Step generation
        if "Python" in tech_stack:
            plan["steps"].append("Prepare Python environment")

        if "Flask" in tech_stack:
            plan["steps"].append("Expose Flask app on port 5000")

        if not analysis.get("dockerization_ready", False):
            plan["steps"].append("Create Dockerfile")

        # 🔹 Dockerfile generation
        plan["dockerfile"] = self.generate_dockerfile(tech_stack)

        # 🔹 Deployment steps
        plan["deployment"] = [
            "Build Docker image",
            "Push to container registry",
            "Deploy on Vultr instance"
        ]

        return plan

    def generate_dockerfile(self, tech_stack):
        if "Python" in tech_stack:
            return """
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
"""
        return "# Unsupported tech stack"