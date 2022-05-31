# _*_ encoding=utf-8 _*_

from ast import keyword
import configparser
import tweepy
import pandas as pd

# load config
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

print(api_key,api_key_secret,access_token,access_token_secret)

# authentication
auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


class Linstener(tweepy.Stream):
    tweets = []
    limit = 10
    def on_status(self, status):
        #  super().on_status(status) 
        # print(status.user.screen_name + ': ' + status.text)
        self.tweets.append(status)
        if len(self.tweets) == self.limit:
            self.disconnect()
     
         

stream_tweet = Linstener(
     api_key,
    api_key_secret,
    access_token,
    access_token_secret)

# stream by keywords
# keyword = ["Cats"]
# stream_tweet.filter(track=keyword)

# stream by user
users = ['gzwilly1']
user_ids = []

for user in users:
    user_ids.append(api.get_user(screen_name=user).id)
    
print(user_ids)
exit()

    

columns = ["User","Tweet"]
data = []
for item in stream_tweet.tweets:
    if not item.truncated :
        data.append([item.user.screen_name,item.text])
    else:
        data.append([item.user.screen_name,item.extendeed_tweet['full_text']])
df = pd.DataFrame(data,columns=columns)

print(df)

