
from telegram import Update
from telegram.ext  import CallbackContext , CommandHandler , Application
from database import db2

# 添加监控用户
async def adduser(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args)
    my_db = db2.MysqlHelper()
    sql = 'INSERT INTO user(tweet_user) VALUES ("'+ text_caps +'")'
    my_db.delete_one(sql)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="添加监控用户"+ text_caps)

# 添加移除用户
async def deluser(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args)
    my_db = db2.MysqlHelper()
    sql = 'delete from `user` where tweet_user="'+text_caps+'"'
    print(sql)
    result = my_db.delete_one(sql)
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="清空监控用户"+ text_caps ,
        reply_to_message_id=update.message.message_id
        )
    
async def list(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args)
    my_db = db2.MysqlHelper()
    sql = "select * from user" 
    result = my_db.get_all(sql)
    users =""
    for item in result:
        users+=item[0]+" , "
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="监控列表"+ users ,
        reply_to_message_id=update.message.message_id
    )
    
    
def register_handlers(application : Application):
    adduser_handler = CommandHandler('adds', adduser)
    deluser_handler = CommandHandler('dels', deluser)
    list_handler = CommandHandler('lists', list)
    application.add_handler(adduser_handler)
    application.add_handler(deluser_handler)
    application.add_handler(list_handler)