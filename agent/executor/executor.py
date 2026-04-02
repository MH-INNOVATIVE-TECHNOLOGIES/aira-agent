import os
import subprocess
from agent.Healer.healer import Healer


class Executor:
    def __init__(self):
        self.healer = Healer()

    def execute_plan(self, plan: dict, project_path: str):
        print("\n⚙️ Starting Execution...\n")

        try:
            return self._run(plan, project_path)

        except Exception as e:
            error_msg = str(e)

            print(f"\n❌ Execution failed:\n{error_msg}")

            # 🧠 Diagnose error
            diagnosis = self.healer.diagnose(error_msg)
            print(f"\n🧠 Diagnosis: {diagnosis}")

            # 🔧 Apply fix
            updated_plan = self.healer.apply_fix(diagnosis, plan)

            print("\n🔁 Retrying after applying fix...\n")

            try:
                return self._run(updated_plan, project_path)

            except Exception as retry_error:
                print(f"\n❌ Retry failed:\n{retry_error}")
                return {
                    "status": "failed",
                    "error": str(retry_error),
                    "diagnosis": diagnosis
                }

    def _run(self, plan: dict, project_path: str):
        # 🔹 Step 1: Create Dockerfile
        dockerfile_path = os.path.join(project_path, "Dockerfile")

        with open(dockerfile_path, "w") as f:
            f.write(plan.get("dockerfile", ""))

        print("✅ Dockerfile created")

        # 🔹 Step 2: Build Docker Image
        image_name = "aira-app"

        build_process = subprocess.run(
            ["docker", "build", "-t", image_name, project_path],
            capture_output=True,
            text=True
        )

        if build_process.returncode != 0:
            raise Exception(build_process.stderr)

        print("✅ Docker image built")

        # 🔹 Step 3: Run Container
        run_process = subprocess.run(
            ["docker", "run", "-d", "-p", "5000:5000", image_name],
            capture_output=True,
            text=True
        )

        if run_process.returncode != 0:
            raise Exception(run_process.stderr)

        print("🚀 Container running on port 5000")

        return {
            "status": "success",
            "image": image_name,
            "container_id": run_process.stdout.strip()
        }