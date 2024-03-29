import sys
from crewai import Agent, Task, Crew
import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain.chat_models.openai import ChatOpenAI
from tools import genetic_tool, rsid_tool
from langchain.agents import load_tools

load_dotenv()

defalut_llm = ChatOpenAI(openai_api_base=os.environ.get("OPENAI_API_BASE_URL", "https://api.openai.com/v1"),
                        openai_api_key= os.environ.get("OPENAI_API_KEY"),
                        temperature=0.1,
                        model_name=os.environ.get("MODEL_NAME", "gpt-3.5-turbo"),
                        top_p=0.3)

human_tools = load_tools(["human"])

geneticist = Agent(
  role='Senior Genesicist',
  goal='Answering questions related to genetics',
  backstory=(
    "You are a Senior Genesicist"
    "You have a knack for dissecting complex data and presenting actionable insights."
  ),
  verbose=True,
  allow_delegation=True,
  tools=[genetic_tool, rsid_tool]+human_tools
)


# Create tasks for your agents
task1 = Task(
  description=(
    "You are knowledgeable biologist and geneticist who use information from API calls in genetic_tool and rsid_tool"
  ),
  expected_output='A concise and full information about requested gene of a user',
  agent=geneticist,
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[geneticist],
  tasks=[task1],
  verbose=2
)

# Get your crew to work!
result = crew.kickoff(inputs={"topic": "apoe gene information"})

print("######################")
print(result)