from embeddings import get_embeddings
from vectorstore import search
from openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def answer(question, collection_name):
    vector = get_embeddings([question])[0]
    chunks = search(vector, collection_name, 5)
    context = " ".join(chunks)

    response = client.chat.completions.create(
        model = "gpt-5.4-nano",
        messages = [
            {"role": "system", "content": "Please base your response solely on the context below"},
            {"role": "user", "content": f"{context}. \n\n {question}"}
        ]
    )

    return response.choices[0].message.content





