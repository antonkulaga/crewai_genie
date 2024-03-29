import os
import sys
from langchain.tools import tool
import requests


api_url = "https://api.longevity-genie.info/"

@tool("genetic_tool")
def genetic_tool(input: str) -> str:
    """
    A tool to answer questions about genes.

    Parameters:
    - input: the input that will be used for api calls, should be the name of the gene

    Returns:
    - results_from_api_calls: a text with information about the gene
    """
    response = requests.get(api_url+"gene_lookup/"+ input)
    print("\n\nSearching for...\n\n" + input)
    return response.json()

@tool("rsid_tool")
def rsid_tool(input: str) -> str:
    """
    A tool to answer questions about rsids.

    Parameters:
    - input: the input that will be used for api calls, should be rsid in format "rs1235"

    Returns:
    - results_from_api_calls: a text with information about the rsid
    """
    response = requests.get(api_url+"rsid_lookup/"+ input)
    print("\n\nSearching for...\n\n" + input)
    return response.json()