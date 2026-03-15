from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# ===== ТВОИ ДАННЫЕ =====
BOT_TOKEN = "8575145131:AAERhzW7TTjf3NT1aFEGfkjuDGN_ftMuAvw"
YOUR_ID = 7635015201

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ===== КОМАНДА ДЛЯ ОТПРАВКИ КОДА =====
@dp.message(Command("send"))
async def send_code(message: types.Message):
    if message.from_user.id != YOUR_ID:
        await message.reply("⛔ Не для тебя")
        return
    
    try:
        parts = message.text.split()
        if len(parts) < 3:
            await message.reply("❌ Формат: /send @username 123456")
            return
        
        username = parts[1].replace('@', '')
        code = parts[2]
        
        # Пытаемся отправить код
        try:
            await bot.send_message(
                chat_id=f"@{username}",
                text=f"🔐 Код подтверждения: {code}"
            )
            await message.reply(f"✅ Код отправлен @{username}")
            
        except Exception as e:
            # Если не получается, даём ссылку на старт
            bot_username = (await bot.me()).username
            link = f"https://t.me/{bot_username}?start=code_{code}"
            
            keyboard = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="🔐 Получить код", url=link)]
                ]
            )
            
            await message.reply(
                f"❌ Не могу написать @{username} сам.\n\n"
                f"👉 Отправь ему эту ссылку:\n"
                f"{link}\n\n"
                f"Когда он нажмёт — код придёт автоматом",
                reply_markup=keyboard
            )
        
    except Exception as e:
        await message.reply(f"❌ Ошибка: {e}")

# ===== ОБРАБОТКА НАЖАТИЯ НА ССЫЛКУ =====
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    args = message.text.split()
    
    # Если есть аргумент (код)
    if len(args) > 1 and args[1].startswith('code_'):
        code = args[1].replace('code_', '')
        await message.reply(f"🔐 Твой код подтверждения: {code}")
    else:
        await message.reply("👋 Привет! Я бот для отправки кодов.")

# ===== ЗАПУСК =====
async def main():
    print("✅ Бот запущен")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
