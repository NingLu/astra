# ASTRA - AI Development Assistant

A multi-agent AI assistant built with Strands Agent framework to automate daily software development tasks.

## Features

### 🔧 Development Agent
- VSCode integration with Amazon Q Developer
- AWS CLI resource management
- Git operations and debugging support

### 🎨 Design Agent
- DrawIO integration for architecture diagrams
- System design document generation
- Browser-based design tools

### 💬 Communication Agent
- Outlook email management
- Slack messaging and notifications
- Amazon Chime integration

### 📋 Project Agent
- Asana project management
- Task creation and tracking
- Project status monitoring

### 🖥️ System Agent
- Computer control (click, type, screenshot)
- File system operations
- Cross-platform support (macOS/Linux)

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and tokens
   ```

3. **Update Configuration**
   Edit `config.yaml` with your specific settings.

4. **Run the Assistant**
   ```bash
   python main.py
   ```

## Usage Examples

### Development Tasks
- "open code project /path/to/project"
- "check aws ec2 instances"
- "list lambda functions"

### Design Tasks
- "create architecture diagram"
- "open drawio for system design"

### Communication Tasks
- "check emails in outlook"
- "send slack message to #general"
- "reply to latest email"

### Project Management
- "list asana tasks"
- "create new task: Fix login bug"
- "open asana dashboard"

### System Control
- "take screenshot"
- "click at coordinates 100,200"
- "create file /tmp/test.txt"

## Configuration

### API Keys Required
- **Slack**: Bot token for workspace integration
- **Outlook**: Microsoft Graph API credentials
- **Asana**: Personal access token
- **AWS**: CLI configured with appropriate permissions

### Strands Agent Tools
- Uses official Strands Agent browser-use and computer-use tools
- Enhanced reliability and cross-platform support

## Architecture

The assistant uses a multi-agent architecture where each agent specializes in specific domains:

```
DevAssistant
├── DevelopmentAgent (VSCode, AWS CLI, Git)
├── DesignAgent (DrawIO, Browser)
├── CommunicationAgent (Email, Slack, Chime)
├── ProjectAgent (Asana, Project Management)
└── SystemAgent (Computer Control, File System)
```

Each agent has access to specialized tools and can be invoked independently or in combination for complex workflows.

## Security Notes

- Store sensitive credentials in `.env` file (not tracked in git)
- Use least-privilege access for API tokens
- Review browser automation permissions
- Computer control requires appropriate system permissions

## Contributing

1. Fork the repository
2. Create feature branch
3. Add tests for new functionality
4. Submit pull request

## License

MIT License - see LICENSE file for details