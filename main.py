import sys
from crewai import Agent, Task, Crew
import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain.chat_models.openai import ChatOpenAI
from tools import gene_tool, rsid_tool
from langchain.agents import load_tools

load_dotenv()

defalut_llm = ChatOpenAI(openai_api_base=os.environ.get("OPENAI_API_BASE_URL", "https://api.openai.com/v1"),
                        openai_api_key= os.environ.get("OPENAI_API_KEY"),
                        temperature=0.1,
                        model_name=os.environ.get("MODEL_NAME", "gpt-4-turbo"),
                        top_p=0.3)

human_tools = load_tools(["human"])

manager = Agent(
  role='Manager and communcator',
  goal='Finding out what the user wants and delegating the task to the corresponding agent',
  backstory=(
    "You are a manager and communicator"
    "You identifying what the user wants and managing other agents, providing them with instructions of what they have to do"
  ),
  verbose=True,
  allow_delegation=True,
  tools=human_tools
)

geneticist = Agent(
  role='Senior Geneticist',
  goal='Answering questions related to genetics',
  backstory=(
    "You are a Senior Geneticist"
    "You have a knack for dissecting complex data and presenting actionable insights."
  ),
  verbose=True,
  allow_delegation=True,
  tools=[gene_tool, rsid_tool]
)


# Create tasks for your agents
task0 = Task(
  description=(
    "You are polite and curious manager that investigates what kind of biology question a user wants to ask"
  ),
  expected_output='Extract of key information that user asked about that you give to another agent that will continue the work on answering the question',
  agent=manager,
)

task1 = Task(
  description=(
    "You are knowledgeable biologist and Geneticist who use information from API calls in gene_tool and rsid_tool"
  ),
  expected_output='A concise and full information about requested gene of a user',
  agent=geneticist,
)



# Instantiate your crew with a sequential process
crew = Crew(
  agents=[manager, geneticist],
  tasks=[task0, task1],
  verbose=2
)

# Get your crew to work!
result = crew.kickoff(inputs={"topic": "apoe gene information"})

print("######################")
print(result)