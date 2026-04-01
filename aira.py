import os
from dotenv import load_dotenv
import requests

# Aira's Core Logic Imports (Jo humne pehle banaye thay)
# Note: In files ka hona zaroori hai aapke folder mein
from agent_logic import generate_dockerfile
from deploy_agent import install_docker_on_remote

class AiraAgent:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("VULTR_API_KEY")
        self.api_url = os.getenv("VULTR_API_URL")
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
        print("--- AIRA AGENT INITIALIZED ---")

    def run_deployment_pipeline(self):
        print("\nAira is starting the deployment process...")
        
        # 1. Analyze & Generate Dockerfile (Noor's Code)
        generate_dockerfile(app_type="python")
        
        # 2. Setup Infrastructure (Saira's Architecture)
        print("Aira is provisioning the server on Vultr...")
        # Mock logic to get IP
        server_ip = "192.168.1.100" 
        
        # 3. Install Environment
        install_docker_on_remote(server_ip, "root", "securepassword123")
        
        print("\n--- DEPLOYMENT BY AIRA COMPLETED SUCCESSFULLY ---")

if __name__ == "__main__":
    aira = AiraAgent()
    aira.run_deployment_pipeline()