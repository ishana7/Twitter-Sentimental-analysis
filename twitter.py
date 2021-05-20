#TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

#TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

from textblob import TextBlob
import pandas as pd   
import re

df = pd.read_csv(r"D:\LP-1 CHITS CODE\DA\A4_twitter\traintwi.csv",usecols=['tweet'])
    
def get_tweet_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))  #creating a tb object
    if analysis.sentiment.polarity  >0 :
        return 'positive'
    elif analysis.sentiment.polarity  <0 :
        return 'negative'
    else:
        return 'neutral'
def clean_tweet(tweet): 
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())   

def get_tweets():
    tweets=[]
    fetched_tweets=df.values.tolist()  #converts serial values to list
    for tweet in fetched_tweets:
        parsed_tweet={}    # empty dictionary to store required params of a tweet 
        parsed_tweet['text']=tweet[0]                # saving text of tweet 
        parsed_tweet['sentiment']=get_tweet_sentiment((tweet[0]))                # saving sentiment of tweet 
        tweets.append(parsed_tweet)                 # appending parsed tweet to tweets list 
    return tweets

tweets=get_tweets()


ptweets = [tweet for tweet in tweets if tweet['sentiment']=='positive']
print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 

ntweets = [tweet for tweet in tweets if tweet['sentiment']=='negative']
print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 

print("Neutral tweets percentage: {} %  ".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))


# printing first 5 positive tweets 
print("\n\nPositive tweets:") 
for tweet in ptweets[:10]: 
    print(tweet['text']) 
  
 # printing first 5 negative tweets 
print("\n\nNegative tweets:") 
for tweet in ntweets[:10]: 
    print(tweet['text'])
