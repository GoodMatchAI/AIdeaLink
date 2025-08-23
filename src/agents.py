from crewai import Agent, LLM
import os

# Initialize the Azure OpenAI LLM using CrewAI's LLM class
azure_llm = LLM(
    model=os.getenv("OPENAI_DEPLOYMENT_NAME"),
    api_key=os.getenv("OPENAI_API_KEY"),
    api_base=os.getenv("OPENAI_ENDPOINT"),
    api_version="2024-02-01",
    api_type="azure"
)

# Define the ProfileAnalysisAgent
profile_analysis_agent = Agent(
    role='Profile Analysis Agent',
    goal='Analyze founder profiles to extract key information.',
    backstory='An expert in understanding startup profiles and identifying key metrics.',
    verbose=True,
    llm=azure_llm,
    allow_delegation=False
)

# Define the InvestorScoutingAgent
investor_scouting_agent = Agent(
    role='Investor Scouting Agent',
    goal='Scout for potential investors based on the founder\'s profile.',
    backstory='A specialist in identifying and vetting potential investors.',
    verbose=True,
    llm=azure_llm,
    allow_delegation=False
)

# Define the MatchmakingAgent
matchmaking_agent = Agent(
    role='Matchmaking Agent',
    goal='Match founders with the best-fit investors and provide detailed reasoning.',
    backstory='A master matchmaker with a deep understanding of the startup ecosystem.',
    verbose=True,
    llm=azure_llm,
    allow_delegation=False
)
