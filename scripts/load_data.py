import os
import json
import weaviate
from dotenv import load_dotenv

load_dotenv()

def get_weaviate_client():
    """Connects to the Weaviate client."""
    url = os.getenv("WEAVIATE_URL", "http://localhost:8080")
    api_key = os.getenv("WEAVIATE_API_KEY")  # Add this to your .env if needed

    if api_key:
        auth_config = weaviate.AuthApiKey(api_key=api_key)
    else:
        auth_config = None

    client = weaviate.Client(
        url=url,
        auth_client_secret=auth_config
    )
    return client

def define_weaviate_schema(client):
    """Defines the Weaviate schema for Founder and Investor objects."""
    founder_schema = {
        "class": "Founder",
        "description": "A startup founder seeking investment.",
        "properties": [
            {"name": "name", "dataType": ["text"]},
            {"name": "industry", "dataType": ["text"]},
            {"name": "stage", "dataType": ["text"]},
            {"name": "funding_ask", "dataType": ["int"]},
            {"name": "desc", "dataType": ["text"]},
        ]
    }
    investor_schema = {
        "class": "Investor",
        "description": "An investor looking for opportunities.",
        "properties": [
            {"name": "name", "dataType": ["text"]},
            {"name": "interests", "dataType": ["string[]"]},
            {"name": "max_invest", "dataType": ["int"]},
            {"name": "past", "dataType": ["text"]},
            {"name": "desc", "dataType": ["text"]},
        ]
    }

    if not client.schema.exists("Founder"):
        client.schema.create_class(founder_schema)
    if not client.schema.exists("Investor"):
        client.schema.create_class(investor_schema)

def load_profiles_from_json(file_path="profiles.json"):
    """Reads the profiles.json file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def upload_data_to_weaviate(client, profiles):
    """Uploads founder and investor data to Weaviate."""
    with client.batch as batch:
        for founder in profiles["founders"]:
            batch.add_data_object(founder, "Founder")
        for investor in profiles["investors"]:
            batch.add_data_object(investor, "Investor")

if __name__ == "__main__":
    client = get_weaviate_client()
    define_weaviate_schema(client)
    profiles = load_profiles_from_json("profiles.json")
    upload_data_to_weaviate(client, profiles)
    print("Successfully ingested data into Weaviate.")
