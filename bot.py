import twitter
from decouple import config
import os

api_client = twitter.Api(
	consumer_key=config('CONSUMER_KEY'),
	consumer_secret=config('CONSUMER_SECRET'),
	access_token_key=config('ACCESS_TOKEN_KEY'),
	access_token_secret=config('ACCESS_TOKEN_SECRET')
)

#Checking credentials out
print(api_client.VerifyCredentials())

#Posting a Twit
'''
result = api_client.PostUpdate('I love python-twitter!')
print(result)
'''

#image path
image_path = os.path.abspath('/home/ana/Downloads/imageCat.jpg')

result = api_client.PostUpdate("Cat code", media=image_path)
print(result)