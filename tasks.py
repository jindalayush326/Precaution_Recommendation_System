from crewai import Task
from tools import tool
from agents import (
    news_research_agent,
    precaution_agent,
    report_generation_agent,
)

# 1. News Research and Summarization Task
news_research_task = Task(
    description="Research and summarize the top news article related to {input_text}.",
    expected_output="A four-sentence summary of the top news article.",
    tools=[tool],
    agent=news_research_agent,
)

# 2. Precaution Recommendation Task
precaution_task = Task(
    description="Generate three precautionary steps based on the summary of the news article.",
    expected_output="Three precautionary steps to mitigate potential risks.",
    tools=[tool],
    agent=precaution_agent,
)

# 3. Comprehensive Report Generation Task
report_generation_task = Task(
    description="Compile the news summary and precautionary steps into a comprehensive report and send it to {email}.",
    expected_output="A detailed report containing the news summary and precautionary steps, sent to the provided email.",
    tools=[tool],
    agent=report_generation_agent,
    async_execution=False,  # This can be adjusted based on your needs
)
