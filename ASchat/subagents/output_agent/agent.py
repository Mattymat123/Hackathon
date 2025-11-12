from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from .prompt import qa_prompt
from .tools import export_to_pdf

from ...config import config

output_agent = Agent(
    model="gemini-2.5-flash",
    name="output_agent",
    description="Generates the final output for the user and exports it to PDF.",
    instruction=qa_prompt,
    output_key="QA_output",
    tools=[FunctionTool(export_to_pdf)],
    #after_agent_callback=suppress_output_callback,
)
