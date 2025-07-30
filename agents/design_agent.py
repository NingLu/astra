from strands_agent import Agent, tool
from typing import Dict, Any
from ..tools.browser_tool import BrowserTool

class DesignAgent(Agent):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(name="DesignAgent")
        self.browser = BrowserTool(config.get("browser", {}))
    
    @tool
    async def create_diagram(self, diagram_type: str = "architecture") -> str:
        """Create new diagram in DrawIO"""
        return await self.browser.open_drawio(diagram_type)
    
    @tool
    async def open_drawio_file(self, file_path: str) -> str:
        """Open existing DrawIO file"""
        return await self.browser.open_drawio_file(file_path)
    
