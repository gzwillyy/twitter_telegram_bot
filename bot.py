from multiprocessing import pool
import os
import pprint
import time
try:
   import telegram
except:
    os.system("pip3 install python-telegram-bot -U --pre")

from create_bot import application
from handlers import client ,manage,inline
from telegram.ext import CommandHandler,CallbackContext
from telegram import Update
from database import db2

async def callback_alarm(context: CallbackContext):
    context.job.context
    my_db = db2.MysqlHelper()
    sql = "select * from queue"
    queue = my_db.get_all(sql)
   
    if len(queue) > 0 :
        ids = [ str(item[0]) for item in queue]
        # 查询
        sql = 'SELECT * FROM  `tweets` where tweet_id in ({});'.format(','.join(ids))
        tweets = my_db.get_all(sql)
        
        # 推送 
        for item in tweets:
            # 删除
            sql_d = 'delete from queue where tweet_id='+str(item[0])
            my_db.delete_one(sql_d)
            print("+++++++++++++++++++")
            print(sql_d)
            print("+++++++++++++++++++")
            text = """@{}   {}   {}""".format(item[3],item[5],item[4])
            await context.bot.send_message(chat_id=context.job.chat_id, text=text)
    

async def callback_timer(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    name = update.effective_chat.full_name
    # Set the alarm:
    await context.job_queue.run_repeating(callback_alarm,5, context=name, chat_id=chat_id)


# 注册事件
client.register_handlers(application)
manage.register_handlers(application)
inline.register_handlers(application)

timer_handler = CommandHandler('monitor', callback_timer)
application.add_handler(timer_handler)
# 负责初始化和启动应用程序、使用 Telegram 轮询更新
application.run_polling()



# if __name__ == '__main__':
# # async def main():
# #     bot = telegram.Bot("5435176311:AAHZHA5qe6vQHh_-TVu3KVGAPUMC5NcBsoE")
# #     async with bot:
# #         # 获取机器人信息
# #         # print(await bot.get_me())
        
# #         #获取人对机器人的信息
# #         print((await bot.get_updates())[0])
        
# #         await bot.send_message(text='Hi John!', chat_id=1847676416)


# # if __name__ == '__main__':
# #     asyncio.run(main())