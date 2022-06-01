#!/usr/bin/env python3

from aiogram import Bot, Dispatcher, executor, types

    # os.system("pip3 install aiogram")


class Bots:
    def __init__(self, api_key):
        self.api_key = api_key

        # 创建机器人实例
        self.bot = Bot(token=api_key)
        dp = Dispatcher(self.bot)
        
        @dp.message_handler(commands=['start', 'help'])
        async def send_welcome(message: types.Message):
            """当用户发送 `/start` 或 `/help` 命令时，将调用此处理程序
            Args:
                message (types.Message): _description_
            """
            await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
            
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
  

