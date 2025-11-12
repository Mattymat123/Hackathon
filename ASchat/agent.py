from google.adk.agents import Agent
from . import prompt


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Root orchestrator for vores ASChat Agent',
    instruction=prompt.test_prompt,
)