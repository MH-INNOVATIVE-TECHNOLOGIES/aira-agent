import paramiko
import time

def install_docker_on_remote(ip, username, password):
    print(f"Connecting to new server at {ip}...")
    
    # SSH Client setup
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Asli server par ye login karega, Mock par hum sirf logic test kar rahe hain
        print(f"Logging into {username}@{ip}...")
        
        # Commands jo server par chalni hain
        commands = [
            "sudo apt update -y",
            "sudo apt install docker.io -y",
            "sudo systemctl start docker",
            "docker --version"
        ]
        
        for cmd in commands:
            print(f"Executing: {cmd}")
            # Real deployment mein yahan ssh.exec_command(cmd) hota hai
            time.sleep(1) # Simulation delay
            
        print("\nSUCCESS: Docker is now installed on the remote server!")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Ye IP humein hamare mock server ne di thi
    server_ip = "192.168.1.100" 
    install_docker_on_remote(server_ip, "root", "securepassword123")