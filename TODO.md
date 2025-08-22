# AIdeaLink Project Plan

A step-by-step plan to build the AIdeaLink project for the GoodFin x AWS AI Hack Day Challenge.

## Phase 0: Project Setup & Organization

- [x] Create a `scripts/` directory.
- [x] Move `generate_profiles.py` into `scripts/`.
- [ ] Create a `src/` directory for the core application logic.
- [ ] Create a `.gitignore` file to exclude `venv/`, `__pycache__/`, `.env`, and other non-essential files.
- [ ] Create a `requirements.txt` file and add the dependencies: `crewai`, `weaviate-client`, `comet_ml`, `requests`, `faker`, `python-dotenv`, `friendli`.
- [ ] Create the `.env` file with `FRIENDLI_API_KEY` and `WEAVIATE_URL` variables.
- [ ] Start the Weaviate Docker container.

## Phase 1: Data Ingestion Pipeline

This phase focuses on loading your synthetic data into the Weaviate vector database.

- [ ] **Create `scripts/load_data.py`:**
    - [ ] Add logic to load environment variables from the `.env` file.
    - [ ] Implement a function to connect to the Weaviate client.
    - [ ] Define the Weaviate schema for "Founder" and "Investor" objects.
    - [ ] Add a function to read the `profiles.json` file.
    - [ ] Implement the main logic to iterate through the JSON data and upload each profile to Weaviate.
    - [ ] Add a confirmation message upon successful data ingestion.

## Phase 2: Core Agentic Logic (CrewAI)

This is the core of the hackathon challenge: building the agents that reason and act.

- [ ] **Create `src/tools.py`:**
    - [ ] Define a custom tool for CrewAI agents that can query the Weaviate database.

- [ ] **Create `src/agents.py`:**
    - [ ] Configure the LLM for the agents using FriendliAI.
    - [ ] Define `ProfileAnalysisAgent`.
    - [ ] Define `InvestorScoutingAgent`.
    - [ ] Define `MatchmakingAgent`.

- [ ] **Create `src/crew.py`:**
    - [ ] Import the agents and the Weaviate tool.
    - [ ] Define the tasks for each agent, chaining them together.
    - [ ] Assemble the agents and tasks into a `Crew`.
    - [ ] Integrate Comet for AI observability.

## Phase 3: Application Interface

- [ ] **Create `main.py` in the root directory:**
    - [ ] Import and instantiate your crew from `src/crew.py`.
    - [ ] Create a simple command-line interface (CLI) that prompts a user for input.
    - [ ] Kick off the crew with the user's input.
    - [ ] Print the final, formatted report to the console.

## Phase 4: Finalization & Polish

- [ ] Test the full, end-to-end workflow with multiple founder profiles.
- [ ] Refine the agent prompts to ensure the reasoning and trade-offs are clear.
- [ ] Update the `README.md` with final, accurate usage instructions.
- [ ] Prepare a compelling demo and story for the presentation.