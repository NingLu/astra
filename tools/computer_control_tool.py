from strands_computer_use import ComputerUseTool
from typing import Dict, Any

class ComputerControlTool:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.computer_tool = ComputerUseTool()
    
    async def take_screenshot(self, save_path: str = None) -> str:
        """Take screenshot of the screen"""
        try:
            result = await self.computer_tool.screenshot()
            if save_path and result.get('image'):
                with open(save_path, 'wb') as f:
                    f.write(result['image'])
                return f"Screenshot saved to: {save_path}"
            return "Screenshot taken"
        except Exception as e:
            return f"Error taking screenshot: {e}"
    
    async def click(self, x: int, y: int) -> str:
        """Click at specified coordinates"""
        try:
            await self.computer_tool.click(x, y)
            return f"Clicked at coordinates ({x}, {y})"
        except Exception as e:
            return f"Error clicking: {e}"
    
    async def type_text(self, text: str) -> str:
        """Type text at current cursor position"""
        try:
            await self.computer_tool.type(text)
            return f"Typed text: {text}"
        except Exception as e:
            return f"Error typing text: {e}"