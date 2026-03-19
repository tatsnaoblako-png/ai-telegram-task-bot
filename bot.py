from dotenv import load_dotenv
load_dotenv()

import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from ai_service import get_ai_response

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

# 🔘 КНОПКИ
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💰 Доход"), KeyboardButton(text="📚 Навыки")],
        [KeyboardButton(text="🚀 Рост"), KeyboardButton(text="🧠 Разобрать ситуацию")],
        [KeyboardButton(text="❓ Что ты умеешь")]
    ],
    resize_keyboard=True
)

# ✅ START
@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer(
        "🔥 Я помогу тебе прокачать доход, навыки и цели\n\n👇 Выбери действие:",
        reply_markup=keyboard
    )

# ✅ ОБРАБОТКА
@dp.message()
async def handle_message(message: Message):
    text = message.text.lower()

    if "доход" in text:
        response = get_ai_response("хочу зарабатывать больше")

    elif "навыки" in text:
        response = get_ai_response("хочу обучаться")

    elif "рост" in text:
        response = get_ai_response("хочу развиваться")

    elif "разобрать" in text:
        response = (
            "🧠 Опиши ситуацию:\n\n"
            "- цель\n"
            "- что мешает\n"
            "- что уже пробовал\n\n"
            "Я помогу 🚀"
        )

    elif "что ты умеешь" in text:
        response = (
            "🤖 Я умею:\n\n"
            "💰 Доход\n"
            "📚 Навыки\n"
            "🚀 Рост\n"
            "🧠 Разбор ситуаций"
        )

    else:
        response = get_ai_response(message.text)

    await message.answer(response)

# ▶️ запуск
async def main():
    print("🔥 БОТ С КНОПКАМИ ЗАПУЩЕН")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())