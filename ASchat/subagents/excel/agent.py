from google.adk import Agent
from .tools import list_files, load_excel, list_sheets
from . import prompt

MODEL = "gemini-2.5-flash"

excel_agent = Agent(
    model=MODEL,
    name="excel_agent",
    instruction=prompt.EXCEL_PROMPT,
    output_key="",
    tools=[list_files,
           load_excel,
           list_sheets],
)
