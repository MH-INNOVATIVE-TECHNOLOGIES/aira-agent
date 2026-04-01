import os
import requests
from dotenv import load_dotenv

# Environment variables load karein
load_dotenv()
API_KEY = os.getenv("VULTR_API_KEY")
URL = os.getenv("VULTR_API_URL")

headers = {"Authorization": f"Bearer {API_KEY}"}

def check_status():
    response = requests.get(f"{URL}/account", headers=headers)
    if response.status_code == 200:
        print("Success! Mock Vultr connected.")
        print(f"Account Data: {response.json()}")
    else:
        print(f"Failed! Status: {response.status_code}")

def create_server():
    print("\n--- Creating New Server ---")
    data = {
        "region": "sgp",
        "plan": "vc2-1c-1gb",
        "os_id": 477,
        "label": "CloudShift-Agent-Node"
    }
    # Mock server par request bhejein
    response = requests.post(f"{URL}/instances", headers=headers, json=data)
    if response.status_code == 202:
        print("Success! Server creation initiated.")
        print(f"Server Info: {response.json()}")
    else:
        print(f"Failed to create server. Status: {response.status_code}")

if __name__ == "__main__":
    check_status()
    create_server()