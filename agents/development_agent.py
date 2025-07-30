from strands_agent import Agent, tool
from typing import Dict, Any
from ..tools.vscode_tool import VSCodeTool
from ..tools.aws_cli_tool import AWSCLITool

class DevelopmentAgent(Agent):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(name="DevelopmentAgent")
        self.vscode = VSCodeTool(config.get("vscode", {}))
        self.aws_cli = AWSCLITool(config.get("aws_cli", {}))
    
    @tool
    async def open_vscode_project(self, project_path: str) -> str:
        """Open project in VSCode"""
        return await self.vscode.open_project(project_path)
    
    @tool
    async def create_file(self, file_path: str, content: str = "") -> str:
        """Create new file and open in VSCode"""
        return await self.vscode.create_file(file_path, content)
    
    @tool
    async def list_aws_resources(self, service: str) -> Dict[str, Any]:
        """List AWS resources for a service (ec2, s3, lambda)"""
        return await self.aws_cli.list_resources(service)
    
    @tool
    async def describe_aws_resource(self, service: str, resource_id: str) -> Dict[str, Any]:
        """Describe specific AWS resource"""
        return await self.aws_cli.describe_resource(service, resource_id)
    
