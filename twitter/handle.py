import logging
import snscrape.modules.twitter as sntwitter
import pandas as pd


class Handle:
    limit = 30
    list = []

    def __init__(self):
        logging.info("初始化twitter...")


    def tweetsWithKeywords(self,query):
        """
        按关键词查询推文
        :param query:
        :return:
        """
        self.list = []
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            if len(self.list) == self.limit:
                break
            else:
                self.list.append([
                    tweet.date,
                    tweet.user.username,
                    tweet.content,
                    tweet.url,
                ])

    def tweetsWithUsers(self,username):
        self.list = []
        for tweet in sntwitter.TwitterUserScraper(username).get_items():
            if len(self.list) == self.limit:
                break
            else:
                self.list.append([
                    tweet.date,
                    tweet.user.username,
                    tweet.content,
                    tweet.url,
                ])