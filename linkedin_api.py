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

### MY PROFILE 

# g = application.get_profile()
# print (g)

### PEOPLE (FORBIDDEN - fill the form "https://www.linkedin.com/help/linkedin/ask/API-DVR")

# people = application.search_profile(selectors=[{'people': ['first-name', 'last-name']}], params={'keywords': 'Sgourdas'})
# print(people)


### COMPANIES DICTIONARY

companies = application.search_company(selectors=[{'companies': ['name', 'universal-name', 'website-url', 'specialties']}], params={'keywords': 'Cork education', 'count': 20, 'start': 0})
companies2 = application.search_company(selectors=[{'companies': ['name', 'universal-name', 'website-url', 'specialties']}], params={'keywords': 'Cork education', 'count': 20, 'start': 20})


# print(companies)
element = 0
while True:
        comps = application.search_company(selectors=[{'companies': ['name', 'universal-name', 'website-url', 'specialties']}], params={'keywords': 'Dublin', 'count': 20, 'start': element})
        comps['companies']['_start'] < comps['companies']['_total']
        element += 20
        print (comps['companies']['_start'])
        print (comps['companies']['_total'])

# with open('companies%s.json' % (params['start']), 'w') as outfile:
#             json.dump(response.json(), outfile, indent=4)    