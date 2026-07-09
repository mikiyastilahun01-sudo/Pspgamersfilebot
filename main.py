import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, CommandObject

BOT_TOKEN = "8700959737:AAH6udD6amqjRnXVoSOYZsgDTVSGdiK8wMM"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

CHANNEL_ID = -1004415006792

GAMES_DATABASE = {
    "game01_main": {
        "message_id": 6,
        "caption": "🎮 **Main Game File**\n\nThank you for visiting our website! Download your game file now."
    },
    "game01_texture": {
        "message_id": 7,
        "caption": "🎨 **Game Texture File**\n\nExtract this file to your texture folder to enjoy full graphics."
    },
    "game01_savedata": {
        "message_id": 8,
        "caption": "💾 **Save Data File**\n\nLoad this save data to unlock all features in the game."
    },
    "game01_camera": {
        "message_id": 9,
        "caption": "📷 **Camera Pack File**\n\nEnhance your game graphics with this custom camera angle pack."
    }
}

@dp.message(CommandStart())
async def start_command(message: types.Message, command: CommandObject):
    file_key = command.args
    
    if not file_key:
        await message.answer("👋 Welcome! Please visit our website and click the download link to get your game files.")
        return

    if file_key in GAMES_DATABASE:
        file_info = GAMES_DATABASE[file_key]
        await message.answer("⏳ Fetching your file from our secure server... Please wait a moment.")
        
        try:
            await bot.copy_message(
                chat_id=message.chat.id,
                from_chat_id=CHANNEL_ID,
                message_id=file_info["message_id"],
                caption=file_info["caption"],
                parse_mode="Markdown"
            )
            await message.answer("✅ File downloaded successfully!\n\n🔗 **To get the next file (Texture/Save Data), go back to our website and click the next download button.**")
        except Exception as e:
            await message.answer("⚠️ Error: Could not transfer the file. Make sure the bot is an Admin in the channel.")
            print(f"Error: {e}")
    else:
        await message.answer("❌ Sorry, this link is expired or invalid. Please check the website again.")

async def main():
    print("🤖 Bot is successfully running and waiting for users...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
