#!/usr/bin/env python3

from cgitb import text
from email import message
from random import randint
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

    # os.system("pip3 install aiogram")


class Bots:
    def __init__(self, api_key):
        self.api_key = api_key

        # 创建机器人实例
        self.bot = Bot(token=api_key)
        dp = Dispatcher(self.bot)
        
        button_start_monitor = InlineKeyboardButton(text="开启监控",callback_data="start_monitor")  
        button_stop_monitor = InlineKeyboardButton(text="停止监控",callback_data="stop_monitor")
        button_status_monitor = InlineKeyboardButton(text="运行状态",callback_data="status_monitor")
        keyboard_inline = InlineKeyboardMarkup().add(button_start_monitor,button_stop_monitor,button_status_monitor)
     
        @dp.message_handler(commands=['menu'])
        async def send_welcome(message: types.Message):
            """返回控制菜单

            Args:
                message (types.Message): _description_
            """
            await message.reply("监控菜单",reply_markup=keyboard_inline)
            
        @dp.callback_query_handler(text=["start_monitor","stop_monitor"])
        async def return_mune(call:types.CallbackQuery):
            """控制菜单回调

            Args:
                call (types.CallbackQuery): _description_
            """
            if call.data == "start_monitor":
                await call.message.answer(randint(1,10)) 
            
            if call.data == "stop_monitor":
                await call.message.answer(randint(100,1000))  
                
            if call.data == "status_monitor":
                await call.message.answer(randint(100,1000))
                  
            await call.answer()
            
             
            
        @dp.message_handler(commands=['start'])
        async def send_welcome(message: types.Message):
            """当用户发送 `/start` 或 `/help` 命令时，将调用此处理程序
            
            Args:
                message (types.Message): _description_
            """
            await message.reply("监控已准备就绪")
            await self.bot.send_message(message.from_user.id,message.text)
            
        @dp.message_handler()
        async def echo(message: types.Message):
            """处理聊天中的所有文本消息，只需添加不带过滤器的处理程序
            
            Args:
                message (types.Message): _description_
            """
            await message.answer(message.text)    
        
        # 运行长轮询    
        executor.start_polling(dp, skip_updates=True)
        



if __name__ == '__main__':
    bot = Bots("5435176311:AAHZHA5qe6vQHh_-TVu3KVGAPUMC5NcBsoE")
  

