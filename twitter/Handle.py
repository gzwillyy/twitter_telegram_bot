import logging
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime, timedelta, timezone
import os
try:
    import emoji
except:
    os.system("pip3 install emoji")
    
class Handle():
    limit = 2
    list = []

    def __init__(self):
        logging.info("get twitter...")


    def tweetsWithKeywords(self,query):
        """
        按关键词查询推文
        :param query: (from:elonmusk) until:2020-01-22 since:2020-01-21
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
                    tweet.id,
                ])

    def tweetsWithUsers(self,username):
        """
        查询用户推文
        :param username:
        :return:
        """
        self.list = []
        for tweet in sntwitter.TwitterUserScraper(username).get_items():
        # url: str
        # date: datetime.datetime
        # content: str
        # renderedContent: str
        # id: int
        # user: 'User'
        # replyCount: int
        # retweetCount: int
        # likeCount: int
        # quoteCount: int
        # conversationId: int
        # lang: str
        # source: str
        # sourceUrl: typing.Optional[str] = None
        # sourceLabel: typing.Optional[str] = None
        # outlinks: typing.Optional[typing.List[str]] = None
        # tcooutlinks: typing.Optional[typing.List[str]] = None
        # media: typing.Optional[typing.List['Medium']] = None
        # retweetedTweet: typing.Optional['Tweet'] = None
        # quotedTweet: typing.Optional['Tweet'] = None
        # inReplyToTweetId: typing.Optional[int] = None
        # inReplyToUser: typing.Optional['User'] = None
        # mentionedUsers: typing.Optional[typing.List['User']] = None
        # coordinates: typing.Optional['Coordinates'] = None
        # place: typing.Optional['Place'] = None
        # hashtags: typing.Optional[typing.List[str]] = None
        # cashtags: typing.Optional[typing.List[str]] = None
            if len(self.list) == self.limit:
                break
            else:
                if tweet.inReplyToTweetId == None:
                    tweet_type_text = '推文'
                    tweet_in_reply_to_tweetId =  '0'
                    tweet_in_reply_to_user =  ''
                else:
                    tweet_type_text = '回复'
                    tweet_in_reply_to_tweetId =  str(tweet.inReplyToTweetId)
                    tweet_in_reply_to_user =  tweet.inReplyToUser.username
                    
                self.list.append({
                    "tweet_id":str(tweet.id),
                    "tweet_user":tweet.username,
                    "tweet_date":tweet.date.astimezone(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S'),
                    "tweet_content":emoji.demojize(tweet.content),
                    "tweet_url":tweet.url,
                    "tweet_type_text":tweet_type_text,
                    "tweet_in_reply_to_tweetId":tweet_in_reply_to_tweetId,
                    "tweet_in_reply_to_user":tweet_in_reply_to_user
                })