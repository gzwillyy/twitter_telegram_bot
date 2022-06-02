from cgitb import text
from create_bot import dp, bot
from aiogram import types ,Dispatcher
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


button_start_monitor = InlineKeyboardButton(text="开启监控",callback_data="start_monitor")  
button_stop_monitor = InlineKeyboardButton(text="停止监控",callback_data="stop_monitor")
button_status_monitor = InlineKeyboardButton(text="运行状态",callback_data="status_monitor")
keyboard_inline = InlineKeyboardMarkup().add(button_start_monitor,button_stop_monitor,button_status_monitor)

# @dp.message_handler(commands=['menu'])
async def send_welcome(message: types.Message):
    """返回控制菜单

    Args:
        message (types.Message): _description_
    """
    await message.reply("监控菜单",reply_markup=keyboard_inline)


# @dp.callback_query_handler(text=["start_monitor","stop_monitor"])
async def return_mune(call:types.CallbackQuery):
    """控制菜单回调

    Args:
        call (types.CallbackQuery): _description_
    """
    if call.data == "start_monitor":
        await call.message.answer(1) 
    
    if call.data == "stop_monitor":
        await call.message.answer(2)  
        
    if call.data == "status_monitor":
        await call.message.answer(3)
            
    await call.answer()





def register_handlers_admin(dp : Dispatcher):
    """注册处理函数

    Args:
        dp (Dispatcher): _description_
    """
    dp.register_message_handler(send_welcome,commands=['menu'])
    dp.register_callback_query_handler(return_mune,text=["start_monitor","stop_monitor"])