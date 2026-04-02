class Healer:
    def __init__(self):
        pass

    def diagnose(self, error_message: str):
        """
        Analyze error and return fix strategy
        """

        error_message = error_message.lower()

        # 🔧 Common failure patterns
        if "port is already allocated" in error_message:
            return {
                "type": "port_conflict",
                "fix": "change_port"
            }

        elif "no module named" in error_message:
            return {
                "type": "missing_dependency",
                "fix": "add_to_requirements"
            }

        elif "docker: command not found" in error_message:
            return {
                "type": "docker_missing",
                "fix": "install_docker"
            }

        elif "permission denied" in error_message:
            return {
                "type": "permission",
                "fix": "add_user_to_docker_group"
            }

        else:
            return {
                "type": "unknown",
                "fix": "manual_review"
            }

    def apply_fix(self, diagnosis: dict, plan: dict):
        """
        Modify plan based on fix strategy
        """

        fix = diagnosis["fix"]

        if fix == "change_port":
            print("🔧 Fixing port conflict...")
            plan["deployment"][0] = "Run on different port (5001)"

        elif fix == "add_to_requirements":
            print("🔧 Adding missing dependency...")
            # simplistic — real version parses error
            with open("sample_project/requirements.txt", "a") as f:
                f.write("\nflask")

        elif fix == "install_docker":
            print("⚠️ Docker not installed. Please install manually.")

        elif fix == "add_user_to_docker_group":
            print("⚠️ Run: sudo usermod -aG docker $USER")

        else:
            print("⚠️ Unknown error — manual intervention needed")

        return plan