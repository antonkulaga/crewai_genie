# Assuming these imports are available from your original codebase
from crewai import Agent
from langchain.agents import load_tools
from genetics import tools

human_tools = load_tools(["human"])


manager = Agent(
    role='Manager',
    goal='Finding out what the user wants by asking them questions if they want to know something and delegating the task to the corresponding agent',
    backstory="""Great manager and communicator, always identifying precisely what a user wants and managing other agents in the most efficient way, providing them with instructions of what they have to do""",
    allow_delegation=True,
    verbose=True,
    tools=human_tools,
    max_iter=3,
    human_input=False
)

geneticist = Agent(
    role='Senior Geneticist',
    goal='Answering questions related to genetics',
    backstory="""Always knows everything about genetics, uses lots of databases and genetics to be always up to date on the topic""",
    verbose=True,
    allow_delegation=False,
    tools=[tools.gene_tool, tools.rsid_tool],
    max_iter=3,
    human_input=False
)