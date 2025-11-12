from google.adk.agents import Agent
from .prompt import qa_prompt

from ...config import config

quality_assurance = Agent(
    model="gemini-2.5-flash",
    name="writer",
    description="Edits a technical blog post based on user feedback.",
    instruction=qa_prompt,
    output_key="QA_output",
    #after_agent_callback=suppress_output_callback,
)
