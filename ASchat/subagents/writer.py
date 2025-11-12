from google.adk.agents import Agent

from ..config import config

writer = Agent(
    model=config.critic_model,
    name="writer",
    description="Edits a technical blog post based on user feedback.",
    instruction="""
    You are a professional technical editor. You will be given a blog post and user feedback.
    Your task is to edit the blog post based on the provided feedback.
    The final output should be a revised blog post in Markdown format.
    """,
    output_key="blog_post",
    #after_agent_callback=suppress_output_callback,
)