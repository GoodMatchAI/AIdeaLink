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
- Install dependencies: `pip install crewai weaviate-client comet_ml requests faker`

### Setup
1. Clone the repo: `git clone https://github.com/GoodMatchAI/AIdeaLink.git`
2. Install API keys (e.g., FriendliAI, Weaviate) in a `.env` file:
   ```
   FRIENDLI_API_KEY=your_key
   WEAVIATE_URL=http://localhost:8080
   ```
3. Generate synthetic data: Run `python generate_profiles.py` (see scripts/).
4. Start Weaviate locally: `docker run -d -p 8080:8080 semitechnologies/weaviate`
5. Install and run: `pip install -r requirements.txt` then `python main.py`

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
