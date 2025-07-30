from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from typing import Dict, Any, List

class SlackTool:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.token = config.get("token")
        self.client = WebClient(token=self.token) if self.token else None
    
    async def get_messages(self, channel: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent messages from a channel"""
        if not self.client:
            return [{"error": "Slack token not configured"}]
        
        try:
            response = self.client.conversations_history(
                channel=channel,
                limit=limit
            )
            messages = []
            for message in response["messages"]:
                messages.append({
                    "user": message.get("user", "Unknown"),
                    "text": message.get("text", ""),
                    "timestamp": message.get("ts", "")
                })
            return messages
        except SlackApiError as e:
            return [{"error": f"Slack API error: {e.response['error']}"}]
    
    async def send_message(self, channel: str, message: str) -> Dict[str, Any]:
        """Send message to a channel"""
        if not self.client:
            return {"error": "Slack token not configured"}
        
        try:
            response = self.client.chat_postMessage(
                channel=channel,
                text=message
            )
            return {"success": True, "timestamp": response["ts"]}
        except SlackApiError as e:
            return {"error": f"Slack API error: {e.response['error']}"}
    
    async def get_channels(self) -> List[Dict[str, Any]]:
        """Get list of channels"""
        if not self.client:
            return [{"error": "Slack token not configured"}]
        
        try:
            response = self.client.conversations_list()
            channels = []
            for channel in response["channels"]:
                channels.append({
                    "id": channel["id"],
                    "name": channel["name"],
                    "is_member": channel.get("is_member", False)
                })
            return channels
        except SlackApiError as e:
            return [{"error": f"Slack API error: {e.response['error']}"}]