import telebot
import os
import http.server
import socketserver
import threading

# Your Bot Token
BOT_TOKEN = "8700959737:AAH6udD6amqjRnXVoSOYZsgDTVSGdiK8wMM"
bot = telebot.TeleBot(BOT_TOKEN)

# Channel ID (Starts with -100)
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
    },
    "cod_victory": {
        "message_id": 12,
        "caption": "🎮 **Call of Duty: Road to Victory**\n\nSize: 464.4 MB\n\nEnjoy the classic action on your PSP!"
    }
}

@bot.message_handler(commands=['start'])
def handle_start(message):
    text = message.text.split()
    
    if len(text) < 2:
        bot.reply_to(message, "👋 Welcome! Please visit our website and click the download link to get your game files.")
        return
        
    file_key = text[1]

    if file_key in GAMES_DATABASE:
        file_info = GAMES_DATABASE[file_key]
        bot.reply_to(message, "⏳ Fetching your file from our secure server... Please wait a moment.")
        
        try:
            bot.copy_message(
                chat_id=message.chat.id,
                from_chat_id=CHANNEL_ID,
                message_id=file_info["message_id"],
                caption=file_info["caption"],
                parse_mode="Markdown"
            )
            bot.send_message(
                chat_id=message.chat.id,
                text="✅ File downloaded successfully!\n\n🔗 **To get the next file (Texture/Save Data), go back to our website and click the next download button.**",
                parse_mode="Markdown"
            )
        except Exception as e:
            bot.reply_to(message, "⚠️ Error: Could not transfer the file. Make sure the bot is an Admin in the channel.")
            print(f"Error: {e}")
    else:
        bot.reply_to(message, "❌ Sorry, this link is expired or invalid. Please check the website again.")

# Dummy server to satisfy Render's port requirement
def run_dummy_server():
    port = int(os.environ.get("PORT", 8080))
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"🌍 Serving dummy port on {port}")
        httpd.serve_forever()

# Start dummy server in a separate thread
threading.Thread(target=run_dummy_server, daemon=True).start()

print("🤖 Bot is successfully running...")
bot.infinity_polling()
    
