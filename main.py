# _*_ encoding=utf-8 _*_

import os

try:
    print(0)
except ImportError:
    os.system("pip3 install tweepy")
    os.system("pip3 install tweepy[async]")
    
# pip3 install configparser
# pip3 install pandas