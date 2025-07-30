from strands_agent import Agent, tool
from typing import Dict, Any, List
from ..tools.asana_tool import AsanaTool
from ..tools.browser_tool import BrowserTool

class ProjectAgent(Agent):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(name="ProjectAgent")
        self.asana = AsanaTool(config.get("asana", {}))
        self.browser = BrowserTool(config.get("browser", {}))
    
    @tool
    async def list_tasks(self, project_id: str = None) -> List[Dict[str, Any]]:
        """List tasks from Asana project or workspace"""
        return await self.asana.get_tasks(project_id)
    
    @tool
    async def create_task(self, name: str, project_id: str = None, description: str = "") -> Dict[str, Any]:
        """Create new task in Asana"""
        return await self.asana.create_task(name, project_id, description)
    
    @tool
    async def open_asana(self) -> str:
        """Open Asana in browser"""
        return await self.browser.open_asana()
    
