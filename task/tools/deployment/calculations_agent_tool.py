from typing import Any

from task.tools.deployment.base_agent_tool import BaseAgentTool


class CalculationsAgentTool(BaseAgentTool):

    @property
    def deployment_name(self) -> str:
        return "calculations-agent"
    
    @property
    def name(self) -> str:
        return "calculations_agent_tool"
    
    @property
    def description(self) -> str:
        return "Tool for performing calculations using a calculations agent. Can execute python code to perform complex calculations and return results. Useful for queries that require mathematical computations or data analysis."
    
    @property
    def parameters(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "The query or instruction to send to the Calculations Agent."
                },
                "propagate_history": {
                    "type": "boolean",
                    "default": False,
                    "description": (
                        "Whether to include previous conversation history between the current agent and Calculations Agent. "
                        "When `true`, the Calculations Agent will have access to prior exchanges for context continuity. "
                        "When `false`, each call starts fresh without historical context. "
                        "Note: Only the conversation history between these two agents is shared; interactions with other agents are never included. "
                        "Note2: Should be set to `true` only when the `prompt` lacks sufficient context and the required context exists in the conversation history.")
                },
            },
            "required": [
                "prompt"
            ]
        }


