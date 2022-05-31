import logging
import snscrape.modules.twitter as sntwitter
import pandas as pd


class Handle:
    query = []
    limit = 10
    twitters = []

    def __init__(self, query):
        logging.info("初始化twitter...")
        logging.info("查询 {}".format(query))
        self.query = query

    def tweets(self):

        for tweet in sntwitter.TwitterSearchScraper(self.query).get_items():
            logging.info("初始化twitter...")
            if len(self.twitters) == self.limit:
                break
            else:
                self.twitters.append([
                    tweet.date,
                    tweet.user.username,
                    tweet.content,
                ])