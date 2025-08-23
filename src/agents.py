from crewai import Agent
from crewai.utilities import LiteLLM
import os

# Initialize the Friendli LLM using LiteLLM
friendli_llm = LiteLLM(
    model="friendli/meta-llama-3.1-8b-instruct",
    api_key=os.getenv("FRIENDLI_TOKEN"),
    base_url="https://api.friendli.ai/serverless/v1"
)

# Define the ProfileAnalysisAgent
profile_analysis_agent = Agent(
    role='Profile Analysis Agent',
    goal='Analyze founder profiles to extract key information.',
    backstory='An expert in understanding startup profiles and identifying key metrics.',
    verbose=True,
    llm=friendli_llm,
    allow_delegation=False
)

# Define the InvestorScoutingAgent
investor_scouting_agent = Agent(
    role='Investor Scouting Agent',
    goal='Scout for potential investors based on the founder\'s profile.',
    backstory='A specialist in identifying and vetting potential investors.',
    verbose=True,
    llm=friendli_llm,
    allow_delegation=False
)

# Define the MatchmakingAgent
matchmaking_agent = Agent(
    role='Matchmaking Agent',
    goal='Match founders with the best-fit investors and provide detailed reasoning.',
    backstory='A master matchmaker with a deep understanding of the startup ecosystem.',
    verbose=True,
    llm=friendli_llm,
    allow_delegation=False
)
