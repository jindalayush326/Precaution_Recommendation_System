from crewai import Agent
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import tool

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()
import asyncio

try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
# Defining the base llm model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.environ.get("GOOGLE_API_KEY"),
    temperature=0.5,
    verbose=True
)

def send_email(to_email, subject, body):
    from_email = os.environ.get("FROM_EMAIL")
    password = os.environ.get("EMAIL_PASSWORD")
    smtp_server = os.environ.get("SMTP_SERVER")
    smtp_port = int(os.environ.get("SMTP_PORT"))

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Create a secure SSL context and log in to the email server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

async def generate_report_and_send_email(report, email):
    subject = "Market Research & Precaution Report"
    body = f"Here is your report:\n\n{report}"
    print("Sending email to:", email)
    send_email(email, subject, body)

# Define the agents
news_research_agent = Agent(
    role="News Research and Summarization Agent",
    goal="Research and summarize the top news article related to {input_text}.",
    verbose=True,
    memory=True,
    backstory=("You are a News Research and Summarization Agent responsible for gathering news articles "
               "related to user input. Your goal is to summarize the top article in four sentences."),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)

# 2. Precaution Recommendation Agent
precaution_agent = Agent(
    role="Precaution Recommendation Agent",
    goal="Provide three precautionary steps based on the summary of the top news article.",
    verbose=True,
    memory=True,
    backstory=("You are a Precaution Recommendation Agent responsible for analyzing the summary of a news article "
               "and generating three precautionary steps to mitigate any potential risks."),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)

# 3. Comprehensive Report Generation Agent
report_generation_agent = Agent(
    role="Comprehensive Report Generation Agent",
    goal="Create a comprehensive report combining the news summary and precautionary steps, then send it via email.",
    verbose=True,
    memory=True,
    backstory=("You are a Comprehensive Report Generation Agent responsible for compiling the summary from the News Research Agent "
               "and the precautionary steps from the Precaution Recommendation Agent into a detailed report."),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)