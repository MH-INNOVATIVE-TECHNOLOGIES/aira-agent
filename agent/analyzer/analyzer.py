import os
import json
from google import genai


class Analyzer:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise Exception("❌ GOOGLE_API_KEY not found in environment variables")

        self.client = genai.Client(api_key=api_key)

    def analyze_code(self, code: str):
        try:
            prompt = f"""
You are an expert software architect.

Analyze the following codebase and return STRICT JSON ONLY.

Output format:
{{
  "tech_stack": [],
  "architecture": "",
  "issues": [],
  "modernization_suggestions": [],
  "dockerization_ready": true
}}

Rules:
- Do NOT add explanations
- Do NOT add text before or after JSON
- Output must be valid JSON only

Code:
{code}
"""

            response = self.client.models.generate_content(
                model="gemini-1.5-flash",
                contents=prompt,
            )

            raw_text = response.text.strip()

            # 🔧 Clean common formatting issues
            cleaned = (
                raw_text.replace("```json", "")
                .replace("```", "")
                .strip()
            )

            # 🔍 Extract JSON safely
            try:
                result = json.loads(cleaned)
            except json.JSONDecodeError:
                # Attempt fallback: extract JSON substring
                start = cleaned.find("{")
                end = cleaned.rfind("}") + 1

                if start != -1 and end != -1:
                    json_str = cleaned[start:end]
                    result = json.loads(json_str)
                else:
                    raise Exception("❌ Could not extract valid JSON from response")

            return result

        except Exception as e:
            raise Exception(f"❌ Analyzer Error: {e}")

    def analyze_project(self, project_files: dict):
        """
        project_files = {
            "file1.py": "...",
            "file2.js": "..."
        }
        """

        try:
            combined_code = ""

            for filename, content in project_files.items():
                combined_code += f"\n\n# FILE: {filename}\n{content}"

            return self.analyze_code(combined_code)

        except Exception as e:
            raise Exception(f"❌ Project Analysis Failed: {e}")