import json
from faker import Faker
fake = Faker()

# Mock founders (opportunities)
founders = [
    {"name": fake.name(), "industry": "AI", "stage": "Seed", "funding_ask": 500000, "desc": "Building AI for healthcare diagnostics."},
    {"name": fake.name(), "industry": "SaaS", "stage": "Pre-Seed", "funding_ask": 250000, "desc": "A B2B SaaS platform for remote team collaboration."},
    {"name": fake.name(), "industry": "FinTech", "stage": "Seed", "funding_ask": 1200000, "desc": "Mobile-first neobank for gig economy workers."},
    {"name": fake.name(), "industry": "E-commerce", "stage": "Seed", "funding_ask": 750000, "desc": "Sustainable fashion marketplace with a subscription model."},
    {"name": fake.name(), "industry": "CleanTech", "stage": "Series A", "funding_ask": 5000000, "desc": "Developing next-gen battery technology for EVs."},
    {"name": fake.name(), "industry": "EdTech", "stage": "Pre-Seed", "funding_ask": 150000, "desc": "Gamified learning app for K-12 mathematics."},
    {"name": fake.name(), "industry": "BioTech", "stage": "Seed", "funding_ask": 2000000, "desc": "Using CRISPR for targeted drug delivery systems."},
    {"name": fake.name(), "industry": "Robotics", "stage": "Series A", "funding_ask": 3000000, "desc": "Autonomous warehouse robots to optimize logistics."},
    {"name": fake.name(), "industry": "Web3", "stage": "Seed", "funding_ask": 1500000, "desc": "Decentralized identity verification platform."},
    {"name": fake.name(), "industry": "Consumer Goods", "stage": "Pre-Seed", "funding_ask": 300000, "desc": "Plant-based snacks with a focus on clean ingredients."}
]

# Mock investors
investors = [
    {"name": fake.name(), "interests": ["AI", "Health"], "max_invest": 1000000, "past": "Invested in 3 AI startups", "desc": "Early-stage VC focused on tech."},
    {"name": fake.name(), "interests": ["SaaS", "FinTech"], "max_invest": 2000000, "past": "Lead investor in a successful FinTech exit.", "desc": "Partner at a growth-stage venture fund."},
    {"name": fake.name(), "interests": ["E-commerce", "Consumer Goods"], "max_invest": 500000, "past": "Angel investor with 10+ CPG portfolio companies.", "desc": "Experienced angel focused on direct-to-consumer brands."},
    {"name": fake.name(), "interests": ["CleanTech", "Robotics"], "max_invest": 10000000, "past": "Ex-founder of a robotics company, now investing.", "desc": "Specialist VC for deep tech and hardware."},
    {"name": fake.name(), "interests": ["EdTech", "AI"], "max_invest": 750000, "past": "Invested in 5 EdTech platforms.", "desc": "Early-stage fund with a social impact mission."},
    {"name": fake.name(), "interests": ["BioTech", "Health"], "max_invest": 5000000, "past": "Former pharma exec. Portfolio includes 3 BioTech firms.", "desc": "BioTech-focused venture capital."},
    {"name": fake.name(), "interests": ["Web3", "FinTech"], "max_invest": 1500000, "past": "Early investor in several successful DeFi projects.", "desc": "Crypto-native fund manager."},
    {"name": fake.name(), "interests": ["SaaS"], "max_invest": 250000, "past": "Multiple seed-stage SaaS investments.", "desc": "Angel investor looking for B2B software solutions."},
    {"name": fake.name(), "interests": ["Logistics", "Robotics", "E-commerce"], "max_invest": 3000000, "past": "Corporate venture arm of a major logistics company.", "desc": "CVC focused on supply chain innovation."},
    {"name": fake.name(), "interests": ["AI", "SaaS", "Health"], "max_invest": 1200000, "past": "Invested across 15 companies in the last 3 years.", "desc": "Generalist investor with a tech focus."}
]

with open('profiles.json', 'w') as f:
    json.dump({"founders": founders, "investors": investors}, f, indent=4)

print("Successfully generated and saved profiles.json")