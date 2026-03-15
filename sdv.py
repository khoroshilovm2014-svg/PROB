import asyncio
from aiogram import Bot, Dispatcher, types
import logging

# Токен и админ
TOKEN = "8575145131:AAERhzW7TTjf3NT1aFEGfkjuDGN_ftMuAvw"
ADMIN_ID = 7635015201

# Включаем логи
logging.basicConfig(level=logging.INFO)

# Создаем бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

# ===== ОБРАБОТКА /start =====
@dp.message(lambda msg: msg.text == "/start")
async def start_command(message: types.Message):
    print(f"Получен /start от {message.from_user.id}")
    if message.from_user.id != ADMIN_ID:
        await message.answer("⛔ Ты не админ")
        return
    
    await message.answer(
        "✅ Бот работает!\n"
        "Используй: /code @username 123456"
    )

# ===== ОБРАБОТКА /code =====
@dp.message(lambda msg: msg.text and msg.text.startswith("/code"))
async def code_command(message: types.Message):
    print(f"Получен /code от {message.from_user.id}")
    
    if message.from_user.id != ADMIN_ID:
        return
    
    try:
        # Разбираем команду
        parts = message.text.split()
        if len(parts) != 3:
            await message.answer("❌ Формат: /code @username 123456")
            return
        
        username = parts[1].replace("@", "")
        code = parts[2]
        
        # Отправляем код
        await bot.send_message(
            chat_id=f"@{username}",
            text=f"🔐 Код: {code}"
        )
        
        await message.answer(f"✅ Отправлено @{username}")
        
    except Exception as e:
        await message.answer(f"❌ Ошибка: {e}")

# ===== ЗАПУСК =====
async def main():
    print("🚀 Бот ЗАПУЩЕН! Жду команды...")
    print(f"Твой ID: {ADMIN_ID}")
    print("Пиши /start в Telegram")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())