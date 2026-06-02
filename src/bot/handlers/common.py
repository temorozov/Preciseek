from aiogram import Bot, Router, F, types
from aiogram.filters import Command
from rag.embeddings import get_embeddings

from bot.storage import save_user_collection, get_user_collection
from rag.parsedoc import parse_pdf
from rag.chunker import chunk_text
from rag.embeddings import get_embeddings
from rag.vectorstore import add_chunks
from rag.answerer import generate_response

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Скинь свой документ, и я отвечу на любой вопрос по нему")

@router.message(F.document)
async def handle_document(message: types.Message, bot: Bot):
    file_id = message.document.file_id
    file_name = message.document.file_name

    user_id = message.from_user.id
    collection_name = f"{user_id}_{file_name}"
    destination=f"files/{collection_name}"

    await bot.download(file_id, destination)

    parsed_pdf = parse_pdf(destination)
    text = " ".join(page["text"] for page in parsed_pdf)

    chunked_text = chunk_text(text, 500, 100)
    text_embeddings = get_embeddings(chunked_text)

    add_chunks(chunked_text, text_embeddings, collection_name)
    save_user_collection(user_id, collection_name)
    
    await message.answer("Обработано. Задавай вопросы")

@router.message()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    collection_name = get_user_collection(user_id)
    
    if collection_name is None:
        await message.answer("Я жду вашего документа")
        return

    response = generate_response(message.text, collection_name)
    await message.answer(response)

