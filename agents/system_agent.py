from strands_agent import Agent, tool
from strands_computer_use import ComputerUseTool
from typing import Dict, Any, List
from ..tools.file_system_tool import FileSystemTool

class SystemAgent(Agent):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(name="SystemAgent")
        self.computer_tool = ComputerUseTool()
        self.file_system = FileSystemTool(config.get("file_system", {}))
    
    @tool
    async def take_screenshot(self) -> str:
        """Take screenshot of the screen"""
        result = await self.computer_tool.screenshot()
        return "Screenshot taken"
    
    @tool
    async def click_at(self, x: int, y: int) -> str:
        """Click at specified coordinates"""
        await self.computer_tool.click(x, y)
        return f"Clicked at ({x}, {y})"
    
    @tool
    async def type_text(self, text: str) -> str:
        """Type text at current cursor position"""
        await self.computer_tool.type(text)
        return f"Typed: {text}"
    
    @tool
    async def create_file(self, path: str, content: str = "") -> str:
        """Create new file with content"""
        return await self.file_system.create_file(path, content)
    
    @tool
    async def list_directory(self, path: str = ".") -> List[str]:
        """List directory contents"""
        return await self.file_system.list_directory(path)
    
