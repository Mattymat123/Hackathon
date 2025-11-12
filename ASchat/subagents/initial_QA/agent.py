from google.adk.agents import Agent
from . import prompt


QA_agent = Agent(
    model='gemini-2.5-flash',
    name='QA_agent',
    description='QA agent for at atklare brugerens spørgsmål for vores ASChat Agent',
    instruction=prompt.test_prompt,
    tools=[],
    
)