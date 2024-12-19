import tweepy

api_key = ""#put your api key here
api_secret = " "#put your api_secret key here
bearer_token = r" "#put your bearer token key
access_token = " "## put your access token key
access_token_secret = " "## put your access token secret key 

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
#this will create a tweet in my account with this text 
response1 = client.create_tweet(text="Hello Twitter!, this is auto generated")
print(response)

#this will delete the tweet of this id.
tweet_id = 1842644817916125426

response2 = client.delete_tweet(tweet_id)
print(response)
