
from telegram import Update
from telegram.ext  import CallbackContext , CommandHandler , Application

# 我们定义一个处理特定类型消息的函数
async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    # update.effective_chat 新通知的信息
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
    
def register_handlers(application : Application):
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)