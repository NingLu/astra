from typing import Dict, Any, List
from strands import Agent
from strands_tools import use_computer

class SystemAgent:
    def __init__(self, config: Dict[str, Any]):
        self.agent = Agent(tools=[use_computer])
    
    def open_calculator(self) -> str:
        """Open calculator application"""
        result = self.agent.tool.use_computer(action="open_app", app_name="Calculator")
        print(result)
        return "Screenshot taken"
    
    # @tool
    # async def click_at(self, x: int, y: int) -> str:
    #     """Click at specified coordinates"""
    #     await self.computer_tool.click(x, y)
    #     return f"Clicked at ({x}, {y})"
    
    # @tool
    # async def type_text(self, text: str) -> str:
    #     """Type text at current cursor position"""
    #     await self.computer_tool.type(text)
    #     return f"Typed: {text}"
    
    # @tool
    # async def create_file(self, path: str, content: str = "") -> str:
    #     """Create new file with content"""
    #     return await self.file_system.create_file(path, content)
    
    # @tool
    # async def list_directory(self, path: str = ".") -> List[str]:
    #     """List directory contents"""
    #     return await self.file_system.list_directory(path)
    
