from aiogram import Bot, Dispatcher, types
import asyncio

# ===== ТВОИ ДАННЫЕ =====
BOT_TOKEN = "8575145131:AAERhzW7TTjf3NT1aFEGfkjuDGN_ftMuAvw"
YOUR_ID = 7635015201  # Твой Telegram ID

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# ===== КОМАНДА ДЛЯ ОТПРАВКИ =====
@dp.message_handler(commands=['send'])
async def send_code(message: types.Message):
    # Проверяем, что это ты (можно убрать если надо)
    if message.from_user.id != YOUR_ID:
        await message.reply("⛔ Не для тебя")
        return
    
    try:
        # Получаем username и код из сообщения
        # Формат: /send @durov 123456
        parts = message.text.split()
        username = parts[1].replace('@', '')
        code = parts[2]
        
        # Отправляем сообщение пользователю
        await bot.send_message(
            chat_id=f"@{username}",  # Telegram поймёт
            text=f"🔐 Код подтверждения: {code}"
        )
        
        await message.reply(f"✅ Код отправлен @{username}")
        
    except Exception as e:
        await message.reply(f"❌ Ошибка: {e}")

# ===== ЗАПУСК =====
if __name__ == '__main__':
    from aiogram import executor
    print("✅ Бот запущен")
    executor.start_polling(dp, skip_updates=True)
