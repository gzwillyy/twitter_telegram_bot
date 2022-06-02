from aiogram import types,Dispatcher
from create_bot import dp, bot
    
    
@dp.message_handler()
async def echo_send(message: types.Message):
    """处理聊天中的所有文本消息，只需添加不带过滤器的处理程序
    
    Args:
        message (types.Message): _description_
    """
    # 发送消息
    await message.answer(message.text)  
    # # 引用回复
    # await message.reply(message.text) 
    # # 如用户在群组里说话 boot dm 给用户
    # await bot.send_message(message.from_user.id,message.text)
    
    
def register_handlers_other(dp : Dispatcher):
    """注册处理函数

    Args:
        dp (Dispatcher): _description_
    """
    dp.register_message_handler(echo_send)