from O365 import Account
from typing import Dict, Any, List

class OutlookTool:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.client_id = config.get("client_id")
        self.client_secret = config.get("client_secret")
        self.account = None
        
        if self.client_id and self.client_secret:
            credentials = (self.client_id, self.client_secret)
            self.account = Account(credentials)
    
    async def authenticate(self) -> bool:
        """Authenticate with Microsoft Graph API"""
        if not self.account:
            return False
        
        if self.account.authenticate(scopes=['basic', 'message_all']):
            return True
        return False
    
    async def get_emails(self, folder: str = "inbox", limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent emails"""
        if not self.account or not await self.authenticate():
            return [{"error": "Authentication failed"}]
        
        try:
            mailbox = self.account.mailbox()
            inbox = mailbox.get_folder(folder_name=folder)
            messages = inbox.get_messages(limit=limit)
            
            emails = []
            for message in messages:
                emails.append({
                    "subject": message.subject,
                    "sender": str(message.sender),
                    "received": str(message.received),
                    "body_preview": message.body_preview,
                    "message_id": message.object_id
                })
            return emails
        except Exception as e:
            return [{"error": f"Error fetching emails: {e}"}]
    
    async def send_email(self, to: str, subject: str, body: str) -> Dict[str, Any]:
        """Send email"""
        if not self.account or not await self.authenticate():
            return {"error": "Authentication failed"}
        
        try:
            mailbox = self.account.mailbox()
            message = mailbox.new_message()
            message.to.add(to)
            message.subject = subject
            message.body = body
            message.send()
            return {"success": True, "message": "Email sent successfully"}
        except Exception as e:
            return {"error": f"Error sending email: {e}"}
    
    async def reply_email(self, message_id: str, reply_body: str) -> Dict[str, Any]:
        """Reply to an email"""
        if not self.account or not await self.authenticate():
            return {"error": "Authentication failed"}
        
        try:
            mailbox = self.account.mailbox()
            message = mailbox.get_message(object_id=message_id)
            reply = message.reply()
            reply.body = reply_body
            reply.send()
            return {"success": True, "message": "Reply sent successfully"}
        except Exception as e:
            return {"error": f"Error replying to email: {e}"}