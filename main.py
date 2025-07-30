#!/usr/bin/env python3
import asyncio
import yaml
from strands_agent import MultiAgent
from typing import Dict, Any
from agents import DevelopmentAgent, DesignAgent, CommunicationAgent, ProjectAgent, SystemAgent

class DevAssistant(MultiAgent):
    def __init__(self, config_path: str = "config.yaml"):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
        # Initialize agents
        agents = [
            DevelopmentAgent(self.config.get("tools", {})),
            DesignAgent(self.config.get("tools", {})),
            CommunicationAgent(self.config.get("tools", {})),
            ProjectAgent(self.config.get("tools", {})),
            SystemAgent(self.config.get("tools", {}))
        ]
        
        super().__init__(agents=agents, name="DevAssistant")
    
    async def process_request(self, request: str) -> str:
        """Process user request using Strands Agent framework"""
        return await self.run(request)
    
    async def run_interactive(self):
        """Run interactive mode"""
        print("DevAssistant - Your AI Development Assistant")
        print("Type 'help' for available commands, 'quit' to exit")
        
        while True:
            try:
                user_input = input("\n> ").strip()
                
                if user_input.lower() in ['quit', 'exit']:
                    break
                elif user_input.lower() == 'help':
                    self._show_help()
                    continue
                
                result = await self.process_request(user_input)
                print(f"Result: {result}")
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Error: {e}")
    
    def _show_help(self):
        """Show available commands"""
        help_text = """
Available Commands:
- Development: "open vscode project", "list aws ec2 instances", "create file"
- Design: "create architecture diagram", "open drawio file"
- Communication: "check emails", "send slack message"
- Project: "list asana tasks", "create task", "open asana"
- System: "take screenshot", "click at coordinates", "create file"
        """
        print(help_text)

async def main():
    assistant = DevAssistant()
    await assistant.run_interactive()

if __name__ == "__main__":
    asyncio.run(main())