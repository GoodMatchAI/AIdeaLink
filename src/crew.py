from crewai import Crew, Task
from src.agents import profile_analysis_agent, investor_scouting_agent, matchmaking_agent
from src.tools import WeaviateQueryTool

# Create an instance of the WeaviateQueryTool
weaviate_tool = WeaviateQueryTool()

# Define the tasks
profile_analysis_task = Task(
    description="Analyze the provided founder profile: {founder_profile}",
    agent=profile_analysis_agent,
    expected_output="A structured analysis of the founder's profile, including industry, stage, and funding ask."
)

investor_scouting_task = Task(
    description="Scout for investors that match the analyzed founder profile.",
    agent=investor_scouting_agent,
    tools=[weaviate_tool],
    expected_output="A list of potential investors with their profiles."
)

matchmaking_task = Task(
    description="Create a final report matching the founder with the top 3 investors, including detailed reasoning and trade-offs.",
    agent=matchmaking_agent,
    context=[profile_analysis_task, investor_scouting_task],
    expected_output="A detailed report with the top 3 investor matches and explanations."
)

# Assemble the crew
aidea_link_crew = Crew(
    agents=[profile_analysis_agent, investor_scouting_agent, matchmaking_agent],
    tasks=[profile_analysis_task, investor_scouting_task, matchmaking_task],
    verbose=True
)

