import subprocess
import os
from typing import Dict, Any

class VSCodeTool:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.command = config.get("command", "code")
    
    async def open_project(self, project_path: str) -> str:
        """Open project in VSCode"""
        try:
            subprocess.run([self.command, project_path], check=True)
            return f"Opened project: {project_path}"
        except subprocess.CalledProcessError as e:
            return f"Error opening project: {e}"
    
    async def create_file(self, file_path: str, content: str = "") -> str:
        """Create a new file and open in VSCode"""
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                f.write(content)
            subprocess.run([self.command, file_path], check=True)
            return f"Created and opened file: {file_path}"
        except Exception as e:
            return f"Error creating file: {e}"
    
    async def open_file(self, file_path: str) -> str:
        """Open existing file in VSCode"""
        try:
            subprocess.run([self.command, file_path], check=True)
            return f"Opened file: {file_path}"
        except subprocess.CalledProcessError as e:
            return f"Error opening file: {e}"