from random import randint
from telegram import InlineQueryResultArticle, InputTextMessageContent , Update
from telegram.ext import InlineQueryHandler ,CallbackContext,Application


async def inlinetw(update: Update, context: CallbackContext.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    
    print("======")
    print(query)
    print("======")
    
    if query == 'tw':
        
        results.append(
            InlineQueryResultArticle(
                id=randint(1,1000000), # 结果的id
                title=str(randint(1,1000000)),     # 结果的标题
                url='https://twitter.com/anndylian/status/1532264113992192000', #结果的url
                hide_url = False, #结果的url 在消息中是否隐藏
                description = 'hahahahahahahhaha',   # 结果的简短描述。
                thumb_url= 'https://pics0.baidu.com/feed/d01373f082025aaf1783d9b5c6e9c56e034f1a2d.png?token=6fd05d9847bd600652cf486b2ffcff70',   # 结果缩略图的 URL。
                thumb_width= 3, # 缩略图宽度。
                thumb_height= 3,    # 缩略图高度。
                input_message_content=InputTextMessageContent('https://twitter.com/anndylian/status/1532264113992192000')
            )
        )
        
    await context.bot.answer_inline_query(update.inline_query.id, results)
    
    
def register_handlers(application : Application):
    inline_tw = InlineQueryHandler(inlinetw)
    application.add_handler(inline_tw)