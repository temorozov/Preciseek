from openai import OpenAI
from typing import List
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embeddings(texts: List[str]):
    response = client.embeddings.create(
        input=texts,
        model="text-embedding-3-small"
    )

    vectors = [item.embedding for item in response.data]
    return vectors