from openai import OpenAI
from typing import List
from config.settings import Settings

settings = Settings()

client = OpenAI(api_key=settings.openai_api_key.get_secret_value())

def get_embeddings(texts: List[str]):
    response = client.embeddings.create(
        input=texts,
        model="text-embedding-3-small"
    )

    vectors = [item.embedding for item in response.data]
    return vectors