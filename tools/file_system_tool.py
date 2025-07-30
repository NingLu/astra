import os
import shutil
from typing import Dict, Any, List

class FileSystemTool:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    async def create_file(self, path: str, content: str = "") -> str:
        """Create a new file with content"""
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w') as f:
                f.write(content)
            return f"Created file: {path}"
        except Exception as e:
            return f"Error creating file: {e}"
    
    async def read_file(self, path: str) -> str:
        """Read file content"""
        try:
            with open(path, 'r') as f:
                content = f.read()
            return content
        except Exception as e:
            return f"Error reading file: {e}"
    
    async def list_directory(self, path: str = ".") -> List[str]:
        """List directory contents"""
        try:
            items = []
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    items.append(f"[DIR] {item}")
                else:
                    items.append(f"[FILE] {item}")
            return items
        except Exception as e:
            return [f"Error listing directory: {e}"]
    
    async def copy_file(self, src: str, dst: str) -> str:
        """Copy file from source to destination"""
        try:
            shutil.copy2(src, dst)
            return f"Copied {src} to {dst}"
        except Exception as e:
            return f"Error copying file: {e}"
    
    async def delete_file(self, path: str) -> str:
        """Delete file"""
        try:
            os.remove(path)
            return f"Deleted file: {path}"
        except Exception as e:
            return f"Error deleting file: {e}"