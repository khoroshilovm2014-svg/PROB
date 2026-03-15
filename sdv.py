from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import os

# ===== ТВОИ ДАННЫЕ =====
BOT_TOKEN = "8575145131:AAERhzW7TTjf3NT1aFEGfkjuDGN_ftMuAvw"  # Вставь сюда токен от @BotFather
YOUR_ID = 7635015201  # Вставь сюда свой Telegram ID

# ===== ИНИЦИАЛИЗАЦИЯ (ПРАВИЛЬНО ДЛЯ 3 ВЕРСИИ) =====
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()  # В 3 версии Dispatcher() БЕЗ АРГУМЕНТОВ

# ===== КОМАНДА СТАРТ =====
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply(
        "🔐 Бот для отправки кодов\n\n"
        "Использование:\n"
        "/send @username 123456 - отправить код пользователю"
    )

# ===== КОМАНДА ДЛЯ ОТПРАВКИ КОДА =====
@dp.message(Command("send"))
async def send_code(message: types.Message):
    # Проверяем, что это админ
    if message.from_user.id != YOUR_ID:
        await message.reply("⛔ У тебя нет прав на использование этой команды")
        return
    
    try:
        # Разбираем сообщение: /send @username 123456
        parts = message.text.split()
        if len(parts) < 3:
            await message.reply("❌ Формат: /send @username 123456")
            return
        
        username = parts[1].replace('@', '')
        code = parts[2]
        
        # Отправляем код пользователю
        await bot.send_message(
            chat_id=f"@{username}",
            text=f"🔐 Код подтверждения: {code}"
        )
        
        await message.reply(f"✅ Код {code} отправлен @{username}")
        
    except Exception as e:
        await message.reply(f"❌ Ошибка: {e}")

# ===== ЗАПУСК БОТА =====
async def main():
    print("✅ Бот запущен и готов к работе")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
