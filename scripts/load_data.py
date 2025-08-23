import os
import json
import weaviate
import weaviate.classes.config as wvc
from dotenv import load_dotenv

load_dotenv()

def get_weaviate_client():
    """Connects to the Weaviate client."""
    return weaviate.connect_to_local(
        host="weaviate",
        port=8080,
        grpc_port=50051,
    )

def define_weaviate_schema(client):
    """Defines the Weaviate schema for Founder and Investor objects."""
    if not client.collections.exists("Founder"):
        client.collections.create(
            name="Founder",
            properties=[
                wvc.Property(name="name", data_type=wvc.DataType.TEXT),
                wvc.Property(name="industry", data_type=wvc.DataType.TEXT),
                wvc.Property(name="stage", data_type=wvc.DataType.TEXT),
                wvc.Property(name="funding_ask", data_type=wvc.DataType.INT),
                wvc.Property(name="desc", data_type=wvc.DataType.TEXT),
            ]
        )
    if not client.collections.exists("Investor"):
        client.collections.create(
            name="Investor",
            properties=[
                wvc.Property(name="name", data_type=wvc.DataType.TEXT),
                wvc.Property(name="interests", data_type=wvc.DataType.TEXT_ARRAY),
                wvc.Property(name="max_invest", data_type=wvc.DataType.INT),
                wvc.Property(name="past", data_type=wvc.DataType.TEXT),
                wvc.Property(name="desc", data_type=wvc.DataType.TEXT),
            ]
        )

def load_profiles_from_json(file_path="profiles.json"):
    """Reads the profiles.json file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def upload_data_to_weaviate(client, profiles):
    """Uploads founder and investor data to Weaviate."""
    founders = client.collections.get("Founder")
    with founders.batch.dynamic() as batch:
        for founder in profiles["founders"]:
            batch.add_object(properties=founder)

    investors = client.collections.get("Investor")
    with investors.batch.dynamic() as batch:
        for investor in profiles["investors"]:
            batch.add_object(properties=investor)

if __name__ == "__main__":
    with get_weaviate_client() as client:
        define_weaviate_schema(client)
        profiles = load_profiles_from_json("profiles.json")
        upload_data_to_weaviate(client, profiles)
        print("Successfully ingested data into Weaviate.")
