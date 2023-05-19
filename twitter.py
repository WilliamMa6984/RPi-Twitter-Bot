#from tweetStream import username

def tweetStart(username, tweet):
	print("1")
	
	import random
	import os
	import re
	import datetime
	from twython import Twython
	
	print("2")
	
	#import variables from auth.py
	from auth import (
		consumer_key,
		consumer_secret,
		access_token,
		access_token_secret
	)
	
	print("3")
	
	#connect to Twitter API using keys
	twitter = Twython(
		consumer_key,
		consumer_secret,
		access_token,
		access_token_secret
	)
	
	print("4")
	
	#image file
	address = "images/"
	categoryList = os.listdir(address)
	print(categoryList)
	
	print("5.1")
	
	#get keywords from tweet
	keywords = [""]
	for i in categoryList:
		print("5.2")
		key = re.findall(i, tweet.lower())
		if key: keywords.append(key[0])
	print(keywords)

	if len(keywords) > 1:
		keywords.pop(0)
		print(keywords)
		print("5.3")
		
	        #Choose random category if multiple found
	        category = random.choice(keywords)
		catAddress = address + category
		
	        print("6")
		
	        fileList = os.listdir(catAddress)
	        print(fileList)
	        images = [""]
	        for i in fileList:
			images.append(catAddress + "/" + i)
	        images.pop(0)

	        #Choose random image
	        imageChoice = random.choice(images)
	        image = open(imageChoice, 'rb')
		
	        print("7")
		
                #upload + get media_id to tweet
	        response = twitter.upload_media(media=image)
	        media_id = [response['media_id']]
		
		print("8")
		
	        #create text message
	        message = "Here's an image of a " + category + " as requested by @" + username + " !\n" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
	        #update message status
	        twitter.update_status(status=message, media_ids=media_id)

	        #console log tweet
		print("Tweeted: " + message + "\n Image:" + category + "\n")
	else:
		print("else1")
		message = "No keywords found, @" + username + " ! Check the list at https://bit.ly/2Wfo6N2 !\n" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

		print("else2")
		#update message status
		twitter.update_status(status=message)

		#console log tweet
		print("Tweeted: " + message)
