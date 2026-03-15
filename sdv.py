from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

# ===== ТВОИ ДАННЫЕ =====
BOT_TOKEN = "8575145131:AAERhzW7TTjf3NT1aFEGfkjuDGN_ftMuAvw"
YOUR_ID = 7635015201

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("code"))
async def send_code(message: types.Message):
    if message.from_user.id != YOUR_ID:
        await message.reply("⛔ Не для тебя")
        return
    
    try:
        parts = message.text.split()
        if len(parts) < 3:
            await message.reply("❌ Формат: /code @username 1234  или  /code 123456789 1234")
            return
        
        target = parts[1].replace('@', '')
        code = parts[2]
        
        # Пробуем отправить
        try:
            # Если target похоже на число - это ID
            if target.isdigit():
                chat_id = int(target)
            else:
                chat_id = f"@{target}"
            
            await bot.send_message(
                chat_id=chat_id,
                text=f"🔐 Код подтверждения: {code}"
            )
            await message.reply(f"✅ Код {code} отправлен")
            
        except Exception as e:
            await message.reply(f"❌ Ошибка: {e}\n\nПользователь должен сначала написать /start боту")
        
    except Exception as e:
        await message.reply(f"❌ Ошибка: {e}")

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    await message.reply(
        f"✅ Твой ID: {user_id}\n"
        f"Твой username: @{username}\n\n"
        f"Передай ID тому, кто будет слать тебе коды."
    )

async def main():
    print("✅ Бот запущен")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
