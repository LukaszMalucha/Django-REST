import json
import os
import env
import tweepy
from tweepy import OAuthHandler

## CREDENTIALS

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')               ## hidden
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')         ## hidden
OAUTH_TOKEN = os.environ.get('OAUTH_TOKEN')                 ## hidden
OAUTH_TOKEN_SECRET = os.environ.get('OAUTH_TOKEN_SECRET')   ## hidden


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)  ## authentication
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET) ## access token

api = tweepy.API(auth)


## ACCESS DATA TRENDS

### http://www.woeidlookup.com/

WRO_WOE_ID = 526363
WAR_WOE_ID = 523920

wroc_trends = api.trends_place(WRO_WOE_ID)
war_trends = api.trends_place(WAR_WOE_ID)

### Build results into lists:

wroc_trends_set = set([trend['name']
                     for trend in wroc_trends[0]['trends']])
                     
war_trends_set = set([trend['name']
                     for trend in war_trends[0]['trends']])                     
                     

### Find common trends

common_trends = set.intersection(wroc_trends_set, war_trends_set)

print(common_trends)
                     