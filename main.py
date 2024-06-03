from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext
from constants import *
from functions import syinon
async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="I'm a bot, please talk to me!")
async def echo(update, context):
    print(3252)
    smth_to_send = syinon(update.message.text, 3, "discord")
    if (update.message.message_thread_id != THEME_CHAT_ID):
        print(2)
        await context.bot.send_message(chat_id=SUPERGROUP_ID, text=smth_to_send, message_thread_id=THEME_CHAT_ID)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.run_polling()