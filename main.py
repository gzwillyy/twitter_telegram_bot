#!/usr/bin/env python3

import logging
import os
from time import time
from lib.log import writelog
from twitter import Handle
from concurrent.futures import ThreadPoolExecutor
import time
from pprint import pp, pprint
from database import db
import asyncio

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

def _search_by_user(username):
    twitter = Handle.Handle()
    twitter.tweetsWithUsers(username)
    return twitter.list    

if __name__ == '__main__':
    initLog()
    # # 关键字搜索推文
    # twitter.tweetsWithKeywords('cats')
    # df = pd.DataFrame(twitter.list, columns=["Date", "Username", "Link", "Tweet"])
    # for item in twitter.list:
    #     logging.info(item)
    # print(df)
    # logging.info("===============================")
    

    # 用户名查找推文
    # twitter.tweetsWithUsers("gzwilly1")
    # df = pd.DataFrame(twitter.list, columns=["Date", "Username", "Link", "Tweet"])
    # for item in twitter.list:
    #     logging.info(item)
    while True:
        loop = asyncio.get_event_loop()
        pool = loop.run_until_complete(db.register())
        
        # 监控用户列表
        sql = f"select tweet_user from user"
        
        tasks = [
            asyncio.ensure_future(db.query(pool, sql)),
        ]
        result = loop.run_until_complete(asyncio.gather(*tasks))

        tweet_in_users = []
        for res in result:
            for item in res:
                    tweet_in_users.append(item[0])

        # 推特查询
        tp = ThreadPoolExecutor(2)
        furures = []
        for username in tweet_in_users:
            furures.append(tp.submit(_search_by_user,username))

        results_get = []
    
        for furure in furures:
            results_get.extend(furure.result())
        
        tweet_ids = [item.get('tweet_id') for item in results_get]
        
        # pprint(results_get)             
        # pprint(tweet_ids)    
        
        # 新推特入库
        if len(tweet_ids) > 0:
            
            start = time.time()
            tmp_tup_str = "','".join(tweet_ids)
            sql = f"select tweet_id from tweets where tweet_id in  ('{tmp_tup_str}')"
            
            tasks = [
                asyncio.ensure_future(db.query(pool, sql)),
            ]
            result = loop.run_until_complete(asyncio.gather(*tasks))
    
            tweet_in_ids = []
            for res in result:
                for item in res:
                    tweet_in_ids.append(item[0])
            
            insert_data = []
            insert_queue = []
            for item in results_get:
                if int(item['tweet_id']) not in tweet_in_ids:
                    insert_data.append(tuple(item.values()))
                    insert_queue.append((int(item['tweet_id']),))

            
            if len(insert_data) > 0 :
                # 批量插入
                sql = "insert into tweets(`tweet_id`, `tweet_user`, `tweet_date`, `tweet_content`, `tweet_url`, `tweet_type_text`, `tweet_in_reply_to_tweetId`, `tweet_in_reply_to_user`) values (%s, %s, %s, %s, %s, %s, %s, %s)"
                sql2 = "insert into queue(`tweet_id`) values (%s)"
                tasks_1 = [
                    asyncio.ensure_future(db.batchInsert(pool, sql, insert_data)),
                    asyncio.ensure_future(db.batchInsert(pool, sql2, insert_queue))
                ]
                result = loop.run_until_complete(asyncio.gather(*tasks_1))
                logging.info("获取到 {} 条推特".format(len(insert_data))) 
            
            loop.run_until_complete(db.close(pool))
            time.sleep(13)
            # loop.close()
            
