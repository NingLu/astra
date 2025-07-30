import requests
from typing import Dict, Any, List

class AsanaTool:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.access_token = config.get("access_token")
        self.workspace_id = config.get("workspace_id")
        self.base_url = "https://app.asana.com/api/1.0"
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        } if self.access_token else {}
    
    async def get_tasks(self, project_id: str = None) -> List[Dict[str, Any]]:
        """Get tasks from project or workspace"""
        if not self.access_token:
            return [{"error": "Asana access token not configured"}]
        
        try:
            if project_id:
                url = f"{self.base_url}/projects/{project_id}/tasks"
            else:
                url = f"{self.base_url}/tasks"
                params = {"workspace": self.workspace_id}
            
            response = requests.get(url, headers=self.headers, params=params if not project_id else None)
            response.raise_for_status()
            
            tasks = []
            for task in response.json()["data"]:
                tasks.append({
                    "gid": task["gid"],
                    "name": task["name"],
                    "completed": task.get("completed", False),
                    "due_date": task.get("due_on"),
                    "assignee": task.get("assignee", {}).get("name") if task.get("assignee") else None
                })
            return tasks
        except requests.RequestException as e:
            return [{"error": f"Asana API error: {e}"}]
    
    async def create_task(self, name: str, project_id: str = None, description: str = "") -> Dict[str, Any]:
        """Create a new task"""
        if not self.access_token:
            return {"error": "Asana access token not configured"}
        
        try:
            url = f"{self.base_url}/tasks"
            data = {
                "data": {
                    "name": name,
                    "notes": description,
                    "projects": [project_id] if project_id else []
                }
            }
            
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            
            task = response.json()["data"]
            return {
                "success": True,
                "task_id": task["gid"],
                "name": task["name"]
            }
        except requests.RequestException as e:
            return {"error": f"Asana API error: {e}"}
    
    async def update_task(self, task_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
        """Update an existing task"""
        if not self.access_token:
            return {"error": "Asana access token not configured"}
        
        try:
            url = f"{self.base_url}/tasks/{task_id}"
            data = {"data": updates}
            
            response = requests.put(url, headers=self.headers, json=data)
            response.raise_for_status()
            
            return {"success": True, "message": "Task updated successfully"}
        except requests.RequestException as e:
            return {"error": f"Asana API error: {e}"}