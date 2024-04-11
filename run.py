import os
import pprint

import click
import loguru
from dotenv import load_dotenv
from typing import Dict, Any

# Assuming these imports are available from your original codebase
from crewai import Crew, Agent, Process
from langchain.chat_models.openai import ChatOpenAI
from langchain.agents import load_tools
from genetics import agents
from genetics import tasks
from loguru import logger

human_tools = load_tools(["human"])

delegation_task = tasks.give_task(agents.manager)
genetic_fetching_task = tasks.fetch_genetic_info_task(agents.geneticist, [delegation_task])

# Use Click to create a CLI command
@click.command()
@click.option('--openai-api-base-url', default="https://api.openai.com/v1", help='Base URL for the OpenAI API')
@click.option('--openai-api-key', envvar='OPENAI_API_KEY', required=True, help='API Key for OpenAI')
@click.option('--model-name', default="gpt-4", help='Model name to use with OpenAI')
@click.option("--topic", default = "APOE gene information", help="Question to ask the model")
def main(openai_api_base_url: str, openai_api_key: str, model_name: str, topic: str):
    load_dotenv()

    defalut_llm = ChatOpenAI(openai_api_base=openai_api_base_url,
                             openai_api_key=openai_api_key,
                             temperature=0.0,
                             model_name=model_name,
                             top_p=0.3)

    # Instantiate your crew with a sequential process
    crew = Crew(
        agents=[agents.manager, agents.geneticist],
        tasks=[delegation_task, genetic_fetching_task],
        process=Process.hierarchical,
        manager_llm=defalut_llm,
        verbose=2,
        memory=True
    )

    # Get your crew to work!
    inputs: Dict[str, Any] = {"topic": topic}
    logger.info(f"INPUTS: {inputs}")
    result = crew.kickoff(inputs=inputs)
    logger.info("RESULTS:")
    logger.info(result)


if __name__ == '__main__':
    main()
