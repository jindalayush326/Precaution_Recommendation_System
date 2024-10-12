import streamlit as st
import re
import sys
from crewai import Crew, Process
import os
import asyncio 
from agents import (
    news_research_agent,
    precaution_agent,
    report_generation_agent,
    generate_report_and_send_email  
)
from tasks import (
    news_research_task,
    precaution_task,
    report_generation_task,
)

# Used to stream sys output on the Streamlit frontend
class StreamToContainer:
    def __init__(self, container):
        self.container = container
        self.buffer = []
        self.colors = ['red', 'green', 'blue', 'orange']
        self.color_index = 0

    def write(self, data):
        # Filter out ANSI escape codes using a regular expression
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)

        # Check if the text contains the specified phrase and apply color
        if "Entering new CrewAgentExecutor chain" in cleaned_data:
            self.color_index = (self.color_index + 1) % len(self.colors)
            cleaned_data = cleaned_data.replace(
                "Entering new CrewAgentExecutor chain",
                f":{self.colors[self.color_index]}[Entering new CrewAgentExecutor chain]",
            )

        # Apply colors to agent names
        for agent_name in ["News Research and Summarization Agent", 
                           "Precaution Recommendation Agent", 
                           "Comprehensive Report Generation Agent"]:
            if agent_name in cleaned_data:
                cleaned_data = cleaned_data.replace(agent_name, f":{self.colors[self.color_index]}[{agent_name}]")

        if "Finished chain." in cleaned_data:
            cleaned_data = cleaned_data.replace("Finished chain.", f":{self.colors[self.color_index]}[Finished chain.]")

        self.buffer.append(cleaned_data)
        if "\n" in data:
            self.container.markdown(''.join(self.buffer), unsafe_allow_html=True)
            self.buffer = []

# Streamlit UI
st.header("News Summarization & Precaution Recommendation System")
st.subheader("Generate a comprehensive report based on news articles!", divider="rainbow", anchor=False)

# User input form
with st.form("form"):
    input_text = st.text_input("Enter a topic or keyword", key="input_text")
    email = st.text_input("Enter your email address", key="email")
    submitted = st.form_submit_button("Submit")

# Process the submission
if submitted:
    with st.status("🤖 **Agents at work...**", expanded=True, state="running") as status:
        with st.container(height=300):
            sys.stdout = StreamToContainer(st)

            # Defining the crew comprising of different agents
            crew = Crew(
                agents=[news_research_agent, precaution_agent, report_generation_agent],
                tasks=[news_research_task, precaution_task, report_generation_task],
                process=Process.sequential,
                verbose=True
            )
            result = crew.kickoff(inputs={"input_text": input_text, "email": email})

        status.update(label="✅ Your Report is ready", state="complete", expanded=False)
    
    st.subheader("Comprehensive Report is ready!", anchor=False, divider="rainbow")
    asyncio.run(generate_report_and_send_email(result, email))
    st.markdown(result)
    

    # Enable file download
    st.download_button(
        label="Download Report",
        data=result,  
        file_name=f"{input_text}_News_Report.txt",  
        mime="text/plain",  
    )
