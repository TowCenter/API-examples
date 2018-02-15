#from twitch_credentials import api_token
import requests

# Implemented during Investigative Techniques with Susan McGregor
# Adapted from:
# https://www.geeksforgeeks.org/get-post-requests-using-python/

# Query 1
# Set up parameters
search_url = 'https://api.opencorporates.com/v0.4/companies/search'

country_code = 'bm'
date_range = '1995-01-01:2000-01-01'

data_params = {
#    'api_token':api_token,
#    'incorporation_date':date_range
    'jurisdiction_code':country_code
}

# Perform GET request
r = requests.get(url = search_url, params=data_params)
print(r.status_code)

data = r.json()

#count = data['results']['total_count']
#print(count)

#for a_company in data['results']['companies']:
#    print(a_company)

# Query 2
bunge_id = '20791'
bunge_country = 'bm' # jurisdiction code

statements_url = \
'https://api.opencorporates.com/v0.4/companies/{}/{}/statements'\
.format(bunge_country, bunge_id)

data_params = {'confidence':'99'}

r = requests.get(url = statements_url, params=data_params)
print(r.status_code)

data = r.json()

# Query 3
officer_url = 'https://api.opencorporates.com/v0.4/officers/search'

data_params = {
    'jurisdiction_code':'us_ny',
    'q':'bloomberg'
}

r = requests.get(url = officer_url, params=data_params)
print(r.status_code)
print(r.url)

print(r.json())
