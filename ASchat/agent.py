from google.adk.agents import Agent
from . import prompt
from .subagents.initial_QA import QA_Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='QA orchestrator for vores ASChat Agent',
    instruction=prompt.orchestrator_prompt,
    tools=[QA_Agent.root_agent],
    
)
