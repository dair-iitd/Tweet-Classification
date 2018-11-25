import io
import sys
import unicodedata
import csv
import os
import random
import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
import sys
f1,f2,f3,f4=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
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
data=[]

with open(f1,"r") as infile:
	i=0
	for line in infile:
		a=get_tweet_sentiment(line)
		if a==1:
			a=0
		else:
			a=1
		data.append((line,a))
inactive=[]
with open(f2,"r") as infile:
	for line in infile:
		inactive.append((line,0))
random.shuffle(inactive)
cnt=0
for i in inactive:
	data.append(i)
	cnt+=1
	if cnt>7000:
		break

random.shuffle(data)
with open(f3,"w") as outfile:
	for dat in data:
		outfile.write(dat[0])
with open(f4,"w") as outfile:
	for dat in data:
		outfile.write(str(dat[1])+"\n")
