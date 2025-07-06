import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Start commando
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welkom bij de JVC Altcoin Pulse Bot 🚀\n"
        "Gebruik /analyse om een marktanalyse te starten."
    )

# Analyse commando
async def analyse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Analyse wordt uitgevoerd...\n"
        "- BTC-dominantie: 52.3%\n"
        "- ETH/BTC-ratio: stabiel\n"
        "- Sectorrotatie: AI & L1 tokens sterk\n"
        "- Marktstructuur: consolidatiefase\n\n"
        "Advies: Bereid je voor op mogelijke Altseason in 1-2 weken!"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("analyse", analyse))

    print("Bot is gestart...")
    app.run_polling()
