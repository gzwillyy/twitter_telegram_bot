from aiogram import types ,Dispatcher
from create_bot import dp, bot

# @dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """当用户发送 `/start` 或 `/help` 命令时，将调用此处理程序
    
    Args:
        message (types.Message): _description_
    """
    try:
        # message.reply("准备就绪")
        await bot.send_message(message.from_user.id,'准备就绪')
        await message.delete()
    except:
        await message.reply("加入机器人到群组: \nhttps://t.me/TwittersMonitorBot")
    
def register_handlers_client(dp : Dispatcher):
    """注册处理函数

    Args:
        dp (Dispatcher): _description_
    """
    dp.register_message_handler(send_welcome,commands=['start'])