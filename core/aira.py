import os
import requests
from dotenv import load_dotenv
from agent.analyzer.analyzer import Analyzer
from agent.planner.planner import Planner
from agent.executor.executor import Executor
from infra.deploy_agent import install_docker_on_remote

load_dotenv()

def call_ai(prompt):
    r = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": "google/gemini-2.0-flash-exp:free",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    return r.json()["choices"][0]["message"]["content"]

class AiraAgent:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("VULTR_API_KEY")
        self.api_url = os.getenv("VULTR_API_URL")
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
        self.analyzer = Analyzer()
        self.planner = Planner()
        self.executor = Executor()
        print("--- AIRA AGENT INITIALIZED ---")

    def run_deployment_pipeline(self, project_files: dict):
        print("\nAira is starting the deployment process...")

        print("\n🔍 Analyzing code...")
        analysis = self.analyzer.analyze_project(project_files)
        print(f"Analysis: {analysis}")

        print("\n📋 Creating plan...")
        plan = self.planner.create_plan(analysis)
        print(f"Plan: {plan}")

        print("\n⚙️ Executing plan...")
        result = self.executor.execute_plan(plan, ".")
        print(f"Result: {result}")

        print("\n--- DEPLOYMENT BY AIRA COMPLETED ---")

if __name__ == "__main__":
    agent = AiraAgent()

    with open("core/legacy_app.py", "r") as f:
        code = f.read()

    project_files = {"legacy_app.py": code}
    agent.run_deployment_pipeline(project_files)
