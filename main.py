#!/usr/bin/env python3

import logging
import os
import time

from lib.log import writelog
from twitter import handle

try:
    import snscrape
except:
    os.system("pip3 install snscrape")
try:
    import pandas as pd
except:
    os.system("pip3 install pandas")

CurFilePath = os.path.abspath(__file__)
# print("CurFilePath=%s" % CurFilePath)
CurFilename = os.path.basename(CurFilePath)
# 'autoSearchGame_YingYongBao.py'

CurFolder = os.path.dirname(CurFilePath)
# print("CurFolder=%s" % CurFolder)

LogFolder = os.path.join(CurFolder, "logs")


def initLog():
    curDatetimeStr = time.strftime("%Y-%m-%d", time.localtime())  # '20231111'
    os.makedirs(LogFolder, exist_ok=True)
    curLogFile = "{}.log".format(curDatetimeStr)
    logFullPath = os.path.join(LogFolder, curLogFile)
    writelog.loggingInit(logFullPath)


if __name__ == '__main__':
    initLog()
    twitter = handle.Handle("cats")
    twitter.tweets()
    df = pd.DataFrame(twitter.twitterlist,columns=["Date","Username","Link","Tweet"])
    print(df)

    # while True:
    #     logging.info("log info")
    #     time.sleep(1)
