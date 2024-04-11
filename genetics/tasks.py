from datetime import datetime
from crewai import Task

def give_task(agent):
    return Task(
        description="""Identifying the information that a user wants to find out on {topic} and delegate it to the corresponding agent and task.""",
        agent=agent,
        async_execution=False,
        expected_output="""A description of a task that the other agent should do."""
    )

def fetch_genetic_info_task(agent, context):
    return Task(
        description="""Extract of key information that user asked about genetics that you
            summarize and bring the essential information to the user. Always provide links for sources as well""",
        agent=agent,
        context=context,
        async_execution=False,
        expected_output="""Detailed information about the {topic}"""
    )