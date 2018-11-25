import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
import sys
def clean_tweet(tweet): 
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())   
def get_tweet_sentiment(tweet): 
    analysis = TextBlob(clean_tweet(tweet) )
    if analysis.sentiment.polarity > 0: 
        return 1
    elif analysis.sentiment.polarity == 0: 
        return 0
    else: 
        return -1
filename=sys.argv[1]
f=open(filename,"r")
sentiment=[0,0,0]
# print(get_tweet_sentiment("today but soon , will decide the fate of this hindu zionists entity .. pak army is now fully geared for this war doctrine .'"))
x=0
for line in f:
    if line!="\n":
        a=get_tweet_sentiment(line)
        sentiment[a]+=1
        # if a==1 and x<10:
        #     print(line)
        #     x+=1
# print(sentiment)
  
    