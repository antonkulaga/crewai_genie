from crewai import Agent
from langchain.agents import load_tools


human_tools = load_tools(["human"])

class biology_crew_agents():
    def manager(self):
        return Agent(
            role='Manager and communcator',
            goal='Finding out what the user wants by asking him a question if they want to know something and delegating the task to the corresponding agent',
            backstory="""Great manager and communicator, identifying always precisely what a user wants
            and managing other agents in the most efficient way, providing them with instructions of what they have to do""",
            allow_delegation=True,
            verbose=True,
            tools=human_tools,
            max_iter=15
        )

    def senior_geneticist(self, tools: list[str]):
        return Agent(
            role='Senior Geneticist',
            goal='Answering questions related to genetics',
            backstory="""Always knows everything about genetics, uses lots of databases and
            papers to be always up to date on the topic""",
            verbose=True,
            allow_delegation=True,
            tools=tools,
            max_iter=3
        )


