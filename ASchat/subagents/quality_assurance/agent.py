from google.adk.agents import Agent
from .prompt import qa_prompt
from .tools import export_to_pdf
from google.adk.tools import FunctionTool

quality_assurance = Agent(
    model="gemini-2.5-flash",
    name="quality_assurance",
    description="Angenten sikrer kvaliteten af aktstykket ved at gennemgå og rette det for fejl og mangler.",
    instruction=qa_prompt,
    output_key="Quality Assurance Output",
    tools=[FunctionTool(export_to_pdf)],
)
