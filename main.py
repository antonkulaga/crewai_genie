import sys
from crewai import Crew, Process
import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain.chat_models.openai import ChatOpenAI
from tools.tools import gene_tool, rsid_tool
from langchain.agents import load_tools
from agents import biology_crew_agents
from tasks import biology_crew_tasks

load_dotenv()

defalut_llm = ChatOpenAI(openai_api_base=os.environ.get("OPENAI_API_BASE_URL", "https://api.openai.com/v1"),
                        openai_api_key= os.environ.get("OPENAI_API_KEY"),
                        temperature=0.1,
                        model_name=os.environ.get("MODEL_NAME", "gpt-4"),
                        top_p=0.3)

agents = biology_crew_agents()
tasks = biology_crew_tasks()

manager = agents.manager()
senior_geneticist = agents.senior_geneticist([gene_tool,rsid_tool])  

creating_task_task = tasks.creating_task_task(manager)
fetch_genetic_info_task = tasks.fetch_genetic_info_task(senior_geneticist, [creating_task_task])

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[manager, senior_geneticist],
  tasks=[creating_task_task, fetch_genetic_info_task],
  process=Process.hierarchical,
  manager_llm=defalut_llm,
  verbose=2
)

# Get your crew to work!
result = crew.kickoff(inputs={"topic": "apoe gene information"})

print("######################")
print(result)