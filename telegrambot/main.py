#!/usr/bin/env python3

import logging
from aiogram import executor, types
from create_bot import dp

async def on_startup(_):
    # 连接数据库等等。。。
    logging.info("telegram bot 启动")
    
from handlers import admin,client,other

# admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
# other.register_handlers_other(dp)


# 运行长轮询    
executor.start_polling(dp, skip_updates=True,on_startup=on_startup)


  

