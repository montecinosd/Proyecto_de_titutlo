import tweepy
# from twitter import OAuth
import json

# import config

consumer_key = "bRwpWaQgDEHcBCGF1zDGHbSdk"
consumer_secret = "q8taVpe97UL2lvn0KaQvuXYNku3oTXHnbV01JARrzb222IY07f"
access_key = "1016921522991255557-VO7IbQdmtwQ6ymU0YPAFPnrvCYVMPA"
access_secret = "CIIlMvp6lY6kFzkH94ymjTYJ1WfvtrulE8HvyAxvG1w0p"

def prueba(request,url_twitter):
	# api = twitter.Api()
	# OAuth process, using the keys and tokens
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	print(url_twitter)
	if(url_twitter == None):
		print("usuario no tiene twitter, return False")
		return False

	index = url_twitter.rfind('/')
	print(index)
	usuario_twitter = url_twitter[index+1:]

	print(usuario_twitter)

	# Creation of the actual interface, using authentication
	api = tweepy.API(auth)
	respuesta_tweets = tweepy.Cursor(api.user_timeline, screen_name='@'+str(usuario_twitter), tweet_mode="extended",exclude_replies=True)
	print("hola")
	print(respuesta_tweets.items())
	tweets = []
	for i in respuesta_tweets.items(50):
		tweets.append(i.full_text)
		# print(i.full_text)
	print("retornando lista:"+str(tweets))
	return json.dumps(tweets)
	# for status in tweepy.Cursor(api.user_timeline, screen_name='@eduardoquiroga', tweet_mode="extended").items():
	# 	print(status.full_text)

