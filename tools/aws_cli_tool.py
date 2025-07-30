import subprocess
import json
from typing import Dict, Any, List

class AWSCLITool:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.profile = config.get("profile", "default")
        self.region = config.get("region", "us-east-1")
    
    async def list_resources(self, service: str) -> Dict[str, Any]:
        """List AWS resources for a service"""
        try:
            if service == "ec2":
                cmd = ["aws", "ec2", "describe-instances", "--profile", self.profile, "--region", self.region]
            elif service == "s3":
                cmd = ["aws", "s3", "ls", "--profile", self.profile]
            elif service == "lambda":
                cmd = ["aws", "lambda", "list-functions", "--profile", self.profile, "--region", self.region]
            else:
                return {"error": f"Unsupported service: {service}"}
            
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return {"output": result.stdout, "service": service}
        except subprocess.CalledProcessError as e:
            return {"error": f"AWS CLI error: {e.stderr}"}
    
    async def describe_resource(self, service: str, resource_id: str) -> Dict[str, Any]:
        """Describe specific AWS resource"""
        try:
            if service == "ec2":
                cmd = ["aws", "ec2", "describe-instances", "--instance-ids", resource_id, 
                       "--profile", self.profile, "--region", self.region]
            elif service == "lambda":
                cmd = ["aws", "lambda", "get-function", "--function-name", resource_id,
                       "--profile", self.profile, "--region", self.region]
            else:
                return {"error": f"Unsupported service: {service}"}
            
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return {"output": result.stdout, "service": service, "resource_id": resource_id}
        except subprocess.CalledProcessError as e:
            return {"error": f"AWS CLI error: {e.stderr}"}