from .embeddings import get_embeddings
from .vectorstore import search
from openai import OpenAI

from config.settings import Settings

settings = Settings()

client = OpenAI(api_key=settings.openai_api_key.get_secret_value())

def generate_response(question, collection_name):
    vector = get_embeddings([question])[0]
    chunks = search(vector, collection_name, 5)
    context = "\n\n".join(chunks)

    system_prompt = []
    system_prompt.append("В тебя был загружен контекст документа (pdf, docx или другого), твоя задача отвечать пользователю на вопросы об этом документе.")
    system_prompt.append(f"Базируй свой ответ на контексте: {context}.")
    system_prompt.append("Если вопрос не про документ — ответить «Этот вопрос не относится к загруженному документу»")

    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": " ".join(system_prompt)},
            {"role": "user", "content": f"{question}"}
        ]
    )

    return response.choices[0].message.content