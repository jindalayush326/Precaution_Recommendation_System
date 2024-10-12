# Precaution Recommendation System

## Description

The Precaution Recommendation System is an AI-driven tool designed to provide users with real-time news updates and relevant precautionary recommendations. This system is powered by multiple agents, including a News Research Agent, a Precaution Recommendation Agent, and a Report Generation Agent. The agents collaborate to research trending news topics, summarize key insights, generate actionable precautions, and deliver the compiled report via email. The application uses technologies like CrewAI, LangChain, Streamlit, Python, and Google Gemini Flash 1.5 LLM.

This tool is ideal for users who want to stay informed about global events and receive practical steps to mitigate associated risks in real-time.

## Demo of the app
A demo showcasing the MPrecaution Recommendation System in action can be viewed at the link below:   
https://precaution-recommendation-system.onrender.com/

<img src="https://github.com/jindalayush326/Precaution_Recommendation_System/blob/main/image/Screenshot%20(6072).png"/>
<img src="https://github.com/jindalayush326/Precaution_Recommendation_System/blob/main/image/Screenshot%20(6073).png"/>
<img src="https://github.com/jindalayush326/Precaution_Recommendation_System/blob/main/image/Screenshot%20(6074).png"/>
<img src="https://github.com/jindalayush326/Precaution_Recommendation_System/blob/main/image/Screenshot%20(6075).png"/>

## Installation

To run this project, follow these steps:

1. Clone this repository to your local machine.
   ```bash
   git clone [https://github.com/jindalayush326/Precaution_Recommendation_System.git]
   ```

2. Navigate to the project directory.
   ```bash
   cd Precaution_Recommendation_System
   ```

3. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```

Set up API keys:

4. Create a .env file in the root directory and add your API keys for Google Gemini Flash 1.5 and SerperAPI as follows:
   GOOGLE_API_KEY=<your-google-api-key>
   EMAIL_HOST=<your-email-host>
   EMAIL_PORT=<your-email-port>
   FROM_EMAIL=<your-email-address>
   EMAIL_PASSWORD=<your-email-password>

## Usage

1. Ensure you have installed all dependencies as instructed above.

2. Run the Streamlit app.
   ```bash
   streamlit run app.py
   ```

3. Access the app through your browser at http://localhost:8501

4. Interact with the app:

   Enter a topic or keyword for news research.
   Provide your email address to receive the generated report.
   Submit to get a comprehensive report containing the news summary and precautionary steps.

## Key Features
1. News Research: The News Research Agent fetches top news articles based on the provided keyword and delivers a summary.
2. Precautionary Recommendations: The Precaution Agent generates actionable steps to mitigate potential risks from the summarized news.
3. Report Generation and Emailing: The system compiles the summary and precautions into a report and sends it directly to the user's email.
4. Streamlit Interface: A user-friendly web interface built with Streamlit that enables easy interaction with the system.

## Technologies Used
1. CrewAI: A framework for building and managing AI agents.
2. LangChain: An API that allows agents to interact with language models for deeper insights.
3. Google Gemini Flash 1.5 LLM: A powerful large language model used to gather and analyze data.
4. Streamlit: A framework to build and run the web-based front-end of the app.
5. SerperAPI: Used for advanced web search and data extraction.
6. Python: The programming language used to build the core logic.
7. SMTP: For sending email reports securely to the user.

## Credits

- [CrewAI](https://www.crewai.com/)
- [Langchain](https://www.langchain.com/)
- [Google Gemini Flash 1.5](https://deepmind.google/technologies/gemini/flash/)
- [Streamlit](https://streamlit.io/)
- [SerperAPI](https://serper.dev/)
- [Python](https://www.python.org/)

## License

This project is licensed under the [MIT License](LICENSE).
```
