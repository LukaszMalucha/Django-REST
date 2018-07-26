import os
import env_linkedin
from linkedin import linkedin
from oauthlib import *


## CREDENTIALS

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')               ## hidden
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')         ## hidden
OAUTH_TOKEN = os.environ.get('OAUTH_TOKEN')                 ## hidden
OAUTH_TOKEN_SECRET = os.environ.get('OAUTH_TOKEN_SECRET')   ## hidden


RETURN_URL = 'http://localhost:8000'

authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                                      OAUTH_TOKEN, OAUTH_TOKEN_SECRET, 
                                                      RETURN_URL, linkedin.PERMISSIONS.enums.values())
                                                      
                                                      
application = linkedin.LinkedInApplication(authentication)        


def multiples(m, count):
    for i in range(count):
        twentiers.append(i + m)
    return twentiers


### COMPANIES DICTIONARY - THROTTLE LIMIT PER TOKEN PER DAY - 500 SEARCHES

companies = application.search_company(selectors=[{'companies': ['name', 'universal-name', 'website-url', 'specialties']}], params={'keywords': 'Tralee'})
total = companies['companies']['_total']
count = int(total / 20)
print(count)
twentiers= [0,] 
multiples(20, count)

print(twentiers)    
    
for element in twentiers:
    comps = application.search_company(selectors=[{'companies': ['name', 'universal-name', 'website-url', 'specialties']}], params={'keywords': 'Tralee', 'count': 20, 'start': element})
    print (comps['companies']['_start'])
    print (comps['companies']['_total'])
    

