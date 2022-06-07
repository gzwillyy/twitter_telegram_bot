import os

try:
   import telegram
except:
    os.system("pip3 install python-telegram-bot -U --pre")

import logging
from telegram.ext  import ApplicationBuilder

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# 创建一个Application对象
application = ApplicationBuilder().token('5435176311:AAHZHA5qe6vQHh_-TVu3KVGAPUMC5NcBsoE').build()

