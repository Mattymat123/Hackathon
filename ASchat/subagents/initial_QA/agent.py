from google.adk.agents import Agent
from . import prompt


QA_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='QA orchestrator for vores ASChat Agent',
    instruction=prompt.test_prompt,
    tools=[],
    
)