import json
import os
import env_linkedin
# from linkedin import linkedin
import oauth2 as oauth
import urllib
from urllib.parse import urlparse

# CREDENTIALS

client_id = os.environ.get('client_id')               ## hidden
client_secret = os.environ.get('client_secret')         ## hidden

consumer = oauth.Consumer(client_id, client_secret)
client = oauth.Client(consumer)


request_token_url      = 'https://api.linkedin.com/uas/oauth/requestToken'

resp, content = client.request(request_token_url, "POST")

## Token exception:

if resp['status'] != '200':
    raise Exception("Invalid response %s." % resp['status'])
    
print (content)
print ("\n")    


# request_token = dict(urlparse.parse(content))

# print ("Request Token:",  "\n")
# print ("- oauth_token        = %s" % request_token['oauth_token'], "\n")
# print ("- oauth_token_secret = %s" % request_token['oauth_token_secret'], "\n")