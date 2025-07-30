from strands_agent import Agent, tool
from typing import Dict, Any
from ..tools.outlook_tool import OutlookTool
from ..tools.slack_tool import SlackTool
from ..tools.chime_tool import ChimeTool

class CommunicationAgent(Agent):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(name="CommunicationAgent")
        self.outlook = OutlookTool(config.get("outlook", {}))
        self.slack = SlackTool(config.get("slack", {}))
        self.chime = ChimeTool(config.get("chime", {}))
    
    @tool
    async def check_emails(self) -> Dict[str, Any]:
        """Check recent emails in Outlook"""
        return await self.outlook.get_emails()
    
    @tool
    async def send_email(self, to: str, subject: str, body: str) -> Dict[str, Any]:
        """Send email via Outlook"""
        return await self.outlook.send_email(to, subject, body)
    
    @tool
    async def send_slack_message(self, channel: str, message: str) -> Dict[str, Any]:
        """Send message to Slack channel"""
        return await self.slack.send_message(channel, message)
    
    @tool
    async def get_slack_messages(self, channel: str) -> Dict[str, Any]:
        """Get recent Slack messages from channel"""
        return await self.slack.get_messages(channel)
    
