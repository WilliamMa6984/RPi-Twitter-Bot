from twython import TwythonStreamer
from twython import TwythonError

from auth import (
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret
)
from twitter import tweetStart

#global username
#global tweet
#Name of Twitter bot
botName = "William62146422"

#Look for tweets
class commandStream(TwythonStreamer):
	def on_success(self, data):
		#If tweet has text, and tweeter is not bot (otherwise it would loop)
		if 'text' in data and data['user']['screen_name'] != botName:
			#Set variables
			username = data['user']['screen_name']
			tweet = data['text']
			print("%s: %s" % (username, tweet))
			#Error handling
			try:
				#Execute tweet function (twitter.py)
				tweetStart(username, tweet)
			except TwythonError as e:
				print("Error: ")
				print(e.error_code)

#Initialise watch for tweets
stream = commandStream(
	consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
)
#Watch for tweets with keyword @Twitter bot
stream.statuses.filter(track=botName)
