from rag.parsedoc import parse_pdf
from rag.chunker import chunk_text
from rag.embeddings import get_embeddings
from rag.vectorstore import add_chunks
from rag.answerer import generate_response
from config.settings import Settings

import asyncio
from aiogram import Bot, Dispatcher
from bot.handlers import common

import os

async def main():
    settings = Settings()

    dp = Dispatcher()
    bot = Bot(token=settings.bot_token.get_secret_value())

    os.makedirs('./files', exist_ok=True)

    dp.include_router(common.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
