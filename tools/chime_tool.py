import requests
from typing import Dict, Any, List

class ChimeTool:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.webhook_url = config.get("webhook_url")
        self.room_id = config.get("room_id")
    
    async def send_message(self, room_id: str, message: str) -> Dict[str, Any]:
        """Send message to Chime room"""
        if not self.webhook_url:
            return {"error": "Chime webhook URL not configured"}
        
        try:
            payload = {
                "Content": message
            }
            
            response = requests.post(self.webhook_url, json=payload)
            response.raise_for_status()
            
            return {"success": True, "message": "Message sent to Chime"}
        except requests.RequestException as e:
            return {"error": f"Chime API error: {e}"}
    
    async def get_messages(self) -> List[Dict[str, Any]]:
        """Get recent messages (placeholder - Chime API limited)"""
        return [{"info": "Chime message retrieval requires specific API access"}]