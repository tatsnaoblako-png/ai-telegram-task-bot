from dotenv import load_dotenv
load_dotenv()

import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart

from ai_service import get_ai_response

# 🔑 бот
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

# 🎛 клавиатура
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💰 Доход"), KeyboardButton(text="📚 Навыки")],
        [KeyboardButton(text="🚀 Рост"), KeyboardButton(text="🧠 Разобрать ситуацию")],
        [KeyboardButton(text="❓ Что ты умеешь")]
    ],
    resize_keyboard=True
)

# ▶️ старт
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🔥 Я помогу тебе прокачать доход, навыки и цели\n\n"
        "👇 Выбери, с чем помочь:",
        reply_markup=keyboard
    )

# ▶️ обработка сообщений
@dp.message()
async def handle_message(message: Message):
    try:
        text = message.text.lower()

        if "доход" in text:
            response = get_ai_response("хочу зарабатывать больше")

        elif "навыки" in text:
            response = get_ai_response("хочу обучаться")

        elif "рост" in text:
            response = get_ai_response("хочу развиваться")

        elif "разобрать" in text:
            response = (
                "🧠 Опиши свою ситуацию:\n\n"
                "- какая цель?\n"
                "- что сейчас не получается?\n"
                "- какие есть ограничения?\n\n"
                "Я разложу по шагам 🚀"
            )

        elif "что ты умеешь" in text:
            response = (
                "🤖 Мои возможности:\n\n"
                "💰 Помогаю увеличить доход\n"
                "📚 Подсказываю, какие навыки качать\n"
                "🚀 Помогаю выстроить план развития\n"
                "🧠 Разбираю твою ситуацию\n\n"
                "Напиши задачу или выбери кнопку 👇"
            )

        else:
            response = get_ai_response(message.text)

    except Exception:
        response = "⚠️ Ошибка, попробуй ещё раз"

    await message.answer(response)

# ▶️ запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())