import logging
import snscrape.modules.twitter as sntwitter
import pandas as pd


class Handle:
    query = []
    limit = 10
    twitterlist = []

    def __init__(self, query):
        logging.info("初始化twitter...")
        logging.info("查询 {}".format(query))
        self.query = query

    def tweets(self):

        for tweet in sntwitter.TwitterSearchScraper(self.query).get_items():
            if len(self.twitterlist) == self.limit:
                break
            else:
                self.twitterlist.append([
                    tweet.date,
                    tweet.user.username,
                    tweet.content,
                ])