from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool


Model="gemini-2.5-flash"



academic_coordinator =  LlmAgent(
    name="academic_coordinator",
    model=Model,
    description=(
        "analyzing seminal papers provided by the users, "
        "providing research advice, locating current papers "
        "relevant to the seminal paper, generating suggestions "
        "for new research directions, and accessing web resources "
        "to acquire knowledge"
    ))
