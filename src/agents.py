from crewai import Agent, LLM
import os

# Initialize the Friendli LLM using CrewAI's LLM class
friendli_llm = LLM(
    model="mistralai/Magistral-Small-2506",
    api_key=os.getenv("FRIENDLI_TOKEN"),
    api_base="https://api.friendli.ai/serverless/v1/chat/completions"
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
