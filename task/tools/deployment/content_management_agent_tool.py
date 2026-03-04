from typing import Any

from task.tools.deployment.base_agent_tool import BaseAgentTool


class ContentManagementAgentTool(BaseAgentTool):

    @property
    def deployment_name(self) -> str:
        return "content-management-agent"
    
    @property
    def name(self) -> str:
        return "content_management_agent_tool"
    
    @property
    def description(self) -> str:
        return "Tool for managing and retrieving content using a content management agent. Can execute queries to store, retrieve, and manage content in a structured way. Can perform RAG Search to find relevant information quickly. Useful for tasks that require handling large amounts of information or maintaining an organized knowledge base."
    
    @property
    def parameters(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "The query or instruction to send to the Content Management Agent."
                },
                "propagate_history": {
                    "type": "boolean",
                    "default": False,
                    "description": (
                        "Whether to include previous conversation history between the current agent and Content Management Agent. "
                        "When `true`, the Content Management Agent will have access to prior exchanges for context continuity. "
                        "When `false`, each call starts fresh without historical context. "
                        "Note: Only the conversation history between these two agents is shared; interactions with other agents are never included. "
                        "Note2: Should be set to `true` only when the `prompt` lacks sufficient context and the required context exists in the conversation history.")
                },
            },
            "required": [
                "prompt"
            ]
        }