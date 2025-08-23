# AIdeaLink

AIdeaLink is an AI-driven tool that matches startup founders with early-stage investors using agentic AI. Built for the GoodFin x AWS [AI Hack Day](https://lu.ma/aws-08-22-25) Challenge, it leverages synthetic profiles and transparent reasoning to connect innovative ideas with capital.

## Overview

This project reimagines wealth management by facilitating founder-investor matchmaking. Powered by tools like CrewAI, FriendliAI, and Weaviate, it turns data into actionable insights with explainable trade-offs—perfect for the "From Prompts to Portfolios" theme.

- **Lanes**: Socialize + Advise
- **Tools Used**: CrewAI (orchestration), FriendliAI (inference), Weaviate (RAG), Comet (observability), Arcade (tools), ScaleKit (auth), Attune (builds), CodeRabbit (reviews)
- **Data**: Synthetic founder/investor profiles

## Features
- Matches founders with investors based on industry, stage, and funding needs.
- Provides transparent reasoning and trade-offs (e.g., "High fit, but prefers later stages").
- Supports collaboration with simulated co-investment suggestions.

## Project Structure
A high-level overview of the project's file structure.

```bash
.
├── .env
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
├── scripts/
│   ├── generate_profiles.py
│   ├── load_data.py
│   └── profiles.json
└── src/
    ├── __init__.py
    ├── agents.py
    ├── crew.py
    └── tools.py
```

## Getting Started

### Prerequisites
- Python 3.9+
- Docker

### Setup
1. Clone the repo: `git clone https://github.com/GoodMatchAI/AIdeaLink.git`
2. Create a `.env` file and add your FriendliAI token:
   ```
   FRIENDLI_TOKEN=your_key
   ```
3. Start the services:
   ```bash
   docker compose up -d
   ```
4. Load the data (only needs to be done once):
   ```bash
   docker compose --profile tools up --build -d
   ```

## Demo

1.  **Attach to the running application:**
    ```bash
    docker compose attach app
    ```
2.  **Enter a founder profile at the prompt.** Here are some examples:
    *   `"AI startup for healthcare diagnostics, seeking $500k in seed funding."`
    *   `"A B2B SaaS platform for remote team collaboration, looking for a $250k pre-seed investment."`
    *   `"Mobile-first neobank for gig economy workers, raising a $1.2M seed round."`
3.  **Review the results.** The application will output the top 3 investor matches with detailed reasoning and trade-offs for each match.

## Usage
- Input a founder profile (e.g., "AI startup, $500k seed").
- Get top 3 investor matches with explanations.
- Explore logs via Comet for transparency.

## Contributing
Built solo for the GoodFin x AWS AI Hack Day Challenge (Aug 22, 2025). Feedback welcome—open an issue or PR!

## License
MIT

## Acknowledgments
- GoodFin x AWS for the challenge.
- xAI and hackathon tools (CrewAI, FriendliAI, etc.) for enabling innovation.