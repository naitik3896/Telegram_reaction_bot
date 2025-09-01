
import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from keep_alive import keep_alive

# ===================================================================
# SETUP INSTRUCTIONS:
# 
# 1. GET YOUR BOT TOKEN:
#    - Message @BotFather on Telegram
#    - Send /newbot and follow instructions
#    - Copy your bot token and replace 'YOUR_BOT_TOKEN_HERE' below
#
# 2. ADD BOT TO CHANNEL:
#    - Go to your Telegram channel
#    - Click channel name -> Administrators -> Add Administrator
#    - Search for your bot username and add it
#    - Give it these permissions:
#      âœ… Post Messages (needed for reactions)
#      âœ… Delete Messages (recommended)
#      âœ… Add New Admins (optional)
#
# 3. RUN ON REPLIT:
#    - Click the "Run" button in Replit
#    - The bot will start and listen for new channel posts
#    - Press Ctrl+C in console to stop the bot
#
# 4. IMPORTANT NOTES:
#    - The bot must be an ADMIN in the channel to react to posts
#    - Only emoji reactions are sent, no text messages
#    - Bot reacts to ALL new posts in channels where it's admin
# ===================================================================

# Replace this with your actual bot token from @BotFather
BOT_TOKEN = '8410221542:AAFFa5Si8BmmMaAk18C686jrweJf1Wkavqw'

# List of positive emoji reactions (no text comments)
positive_emojis = ['❤', '😘', '👍', '😎', '🥰', '🥳']
 # Logging setup
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def react_to_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """React to new posts in channels with random positive emojis only"""
    
    # Get the channel post
    message = update.channel_post
    if not message:
        return

    # Select a random positive emoji
    reaction_emoji = random.choice(positive_emojis)

    try:
        # React with emoji only (no text messages)
        await context.bot.set_message_reaction(
            chat_id=message.chat.id,
            message_id=message.message_id,
            reaction=reaction_emoji,
            is_big=False  # Use small reaction
        )

        logger.info(f"âœ… Reacted to message {message.message_id} in {message.chat.title} with: {reaction_emoji}")

    except Exception as e:
        logger.error(f"âŒ Failed to react to message {message.message_id}: {e}")

def main():
    """Main function to run the bot"""
    
    # Check if bot token is set
    if BOT_TOKEN == 'YOUR_BOT_TOKEN_HERE':
        print("âŒ ERROR: Please set your BOT_TOKEN in main.py")
        print("ðŸ“± Get your token from @BotFather on Telegram")
        return

    # Create application
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add handler for channel posts only
    app.add_handler(MessageHandler(filters.UpdateType.CHANNEL_POST, react_to_channel_post))

    # Start keep-alive web server
    keep_alive()
    
    print("ðŸ¤– Telegram Reaction Bot is starting...")
    print("âœ¨ Bot will react to new channel posts with positive emojis")
    print("ðŸ”§ Make sure the bot is added as ADMIN to your channels")
    print("ðŸŒ Keep-alive server running on port 8080")
    print("ðŸ›‘ Press Ctrl+C to stop the bot")
    print("-" * 50)

    # Start the bot
    app.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
