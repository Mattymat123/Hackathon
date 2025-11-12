from google.adk.agents import Agent

from . import prompt
from google.adk.tools.agent_tool import AgentTool
from .subagents.initial_QA import QA_agent
from .subagents.writer import writer
from .subagents.research import research_agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',

    description='QA orchestrator for vores ASChat Agent',
    instruction=prompt.orchestrator_prompt,
    tools=[
        AgentTool(agent=QA_agent),
        AgentTool(agent=research_agent),
        AgentTool(agent=writer),
    ],
    
)
