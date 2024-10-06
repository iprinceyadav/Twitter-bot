import tweepy

api_key = "1gpQ8vay0UnrCz6N9LN4G6MrT"
api_secret = "ZG6TsPHrJ5xeuh54xG737sg05tIHMhP7l5PxzbQsKAPZKGIrMp"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAC8AwQEAAAAAfS4YQtmI6OH2X5g05C6fws5nWsA%3D6UsMyjD7BysSTzPs2kMoP3jZznnr8cPW1qL4dIGdfFs7RIQJpb"
access_token = "1579348101579608066-Q7DQeIa8gEWlxQeqZG4PgiQSrAGsvI"
access_token_secret = "cy38ctZUftbQcYKAfUqwytYyfkwiQw5f5uO8NiorvRqcL"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

tweet_id = 1842644817916125426

response = client.delete_tweet(tweet_id)
print(response)
