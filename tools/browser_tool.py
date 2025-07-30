from strands_browser_use import BrowserUseTool
from typing import Dict, Any

class BrowserTool:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.browser_tool = BrowserUseTool()
    
    async def open_drawio(self, diagram_type: str = "architecture") -> str:
        """Open DrawIO in browser"""
        try:
            await self.browser_tool.navigate("https://app.diagrams.net/")
            return f"Opened DrawIO for {diagram_type} diagram"
        except Exception as e:
            return f"Error opening DrawIO: {e}"
    
    async def open_drawio_file(self, file_path: str) -> str:
        """Open existing DrawIO file"""
        try:
            await self.browser_tool.navigate(f"https://app.diagrams.net/?open={file_path}")
            return f"Opened DrawIO file: {file_path}"
        except Exception as e:
            return f"Error opening DrawIO file: {e}"
    
    async def open_asana(self) -> str:
        """Open Asana in browser"""
        try:
            await self.browser_tool.navigate("https://app.asana.com/")
            return "Opened Asana"
        except Exception as e:
            return f"Error opening Asana: {e}"