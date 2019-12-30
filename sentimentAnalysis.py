import tweepy
import csv
from textblob import TextBlob

topic = input("Please enter the topic to find sentiment about: ")
fileName = input("Please enter the path of the file to be written to: ")

def findOpinion(polarity):
	if polarity == 0:
		return 'Neutral'
	elif polarity > 0:
		return 'Positive'
	elif polarity < 0:
		return 'Negative'	

consumer_key = input("Please enter the public API key: ")
consumer_secret = input("Please enter the secret API key: ")

access_token = input("Please enter the public access token: ")
access_token_secret = input("Please enter the secret access token: ")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(topic)

# Accessing CSV file

outputFile = open(fileName, 'w', newline = "")
writer = csv.writer(outputFile)

for tweet in public_tweets:
	analysis = TextBlob(tweet.text)
	writer.writerow([tweet.text, findOpinion(analysis.sentiment.polarity)])