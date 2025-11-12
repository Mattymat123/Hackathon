from google.adk import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import google_search
from . import prompt
from ..excel import excel_agent

MODEL = "gemini-2.5-pro"

research_agent = Agent(
    model=MODEL,
    name="research_agent",
    instruction=prompt.RESEARCHER_PROMPT,
    output_key="",
    tools=[google_search,
           AgentTool(agent=excel_agent)],
)