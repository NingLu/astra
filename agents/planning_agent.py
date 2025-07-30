from strands_agent import Agent, tool
from typing import List, Dict, Any

class PlanningAgent(Agent):
    def __init__(self):
        super().__init__(name="PlanningAgent")
    
    @tool
    async def create_workflow_plan(self, goal: str) -> List[Dict[str, Any]]:
        """Break down complex goal into actionable steps"""
        # Simple planning logic
        if "microservice" in goal.lower():
            return [
                {"agent": "development", "action": "create_repo"},
                {"agent": "development", "action": "write_dockerfile"},
                {"agent": "development", "action": "deploy_aws"},
                {"agent": "communication", "action": "send_update"}
            ]
        return [{"agent": "system", "action": "clarify_goal"}]