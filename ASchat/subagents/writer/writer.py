from google.adk.agents import Agent
from .prompt import writer_prompt

from ...config import config

writer = Agent(
    model="gemini-2.5-flash",
    name="writer",
    description="Edits a technical blog post based on user feedback.",
    instruction= writer_prompt,
    output_key="blog_post",
    #after_agent_callback=suppress_output_callback,
)