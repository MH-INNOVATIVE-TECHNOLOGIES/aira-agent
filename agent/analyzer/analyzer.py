import os
from dotenv import load_dotenv
load_dotenv()

class Analyzer:
    def __init__(self):
        print("✅ Analyzer initialized with Mock API")

    def analyze_code(self, code: str):
        return {
            "tech_stack": ["Python", "Flask"],
            "architecture": "Monolithic",
            "issues": ["No containerization", "No environment variables"],
            "modernization_suggestions": ["Dockerize", "Use .env file"],
            "dockerization_ready": True
        }

    def analyze_project(self, project_files: dict):
        combined_code = ""
        for filename, content in project_files.items():
            combined_code += f"\n--- {filename} ---\n{content}\n"
        return self.analyze_code(combined_code)
