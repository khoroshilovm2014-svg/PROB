from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

# ===== ТВОИ ДАННЫЕ =====
BOT_TOKEN = "8575145131:AAERhzW7TTjf3NT1aFEGfkjuDGN_ftMuAvw"  # Твой токен
YOUR_ID = 7635015201  # Твой Telegram ID (fanat metana)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ===== КОМАНДА ДЛЯ ОТПРАВКИ КОДА =====
@dp.message(Command("code"))
async def send_code(message: types.Message):
    # Проверяем, что команда от тебя
    if message.from_user.id != YOUR_ID:
        await message.reply("⛔ Не для тебя")
        return
    
    try:
        # Разбираем команду: /code @username 1234
        parts = message.text.split()
        if len(parts) < 3:
            await message.reply("❌ Формат: /code @username 1234")
            return
        
        username = parts[1].replace('@', '')
        code = parts[2]
        
        # Отправляем сообщение пользователю
        await bot.send_message(
            chat_id=f"@{username}",
            text=f"🔐 Код подтверждения: {code}"
        )
        
        await message.reply(f"✅ Код {code} отправлен @{username}")
        
    except Exception as e:
        await message.reply(f"❌ Ошибка: {e}")

# ===== КОМАНДА СТАРТ =====
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply("Привет! Я бот для отправки кодов.")

# ===== ЗАПУСК =====
async def main():
    print("✅ Бот запущен")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
