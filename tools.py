from dotenv import load_dotenv
from crewai_tools import SerperDevTool
import os

# Load environment variables from .env file
load_dotenv()

# Set the API key for Serper (Google Search Tool)
os.environ["SERPER_API_KEY"] = os.environ.get("SERPER_API_KEY")

# Initialize the SerperDevTool for Google searches
tool = SerperDevTool()
