import json, requests
from foursquarekeys import foursquare_keys

# This is the base URL
base_url = 'https://api.foursquare.com/v2/venues/explore'


# The following mapping contains some keys that are mandatory for the request to be executed successfully
# The mandatory parameters are: 
# 1- client_id
# 2 - client_secret
# 3 - v (version parameter) 
# Some parameters are not mandatory by themselves, but the search is driven by them or some other parameter that has a similar meaning
# For example, we can exclude 'll', but we would have to provide 'near' instead.
# Rest of the parameters are not mandatory
'''
Query 1:
https://api.foursquare.com/v2/venues/explore?client_id=04JOGOUXDKSCL2LDGHWILZDZXB0YUF5Q5NVOQ0CS2FFH3H2D&client_secret=W3N0K22PWTZLITEKUFCXA5UU0KKTJQNLHS1IOD0NQABZIBF4&v=20180323&query=wine&limit=1&near=New York, NY
'''
# Params for Query 1
params = dict(
  client_id=foursquare_keys[0],
  client_secret=foursquare_keys[1],
  v='20180323',
  near='New York, NY',
  query='wine',
  limit=1
)

'''
Query 2:
https://api.foursquare.com/v2/venues/explore?client_id=04JOGOUXDKSCL2LDGHWILZDZXB0YUF5Q5NVOQ0CS2FFH3H2D&client_secret=W3N0K22PWTZLITEKUFCXA5UU0KKTJQNLHS1IOD0NQABZIBF4&v=20180323&section=sights&limit=1&ll=40.716558,-74.004608
'''
# params = dict(
#   client_id=foursquare_keys[0],
#   client_secret=foursquare_keys[1],
#   v='20180323',
#   ll='40.716558,-74.004608',
#   section='sights',
#   limit=1
# )

'''
Query 3:
https://api.foursquare.com/v2/venues/explore?client_id=04JOGOUXDKSCL2LDGHWILZDZXB0YUF5Q5NVOQ0CS2FFH3H2D&client_secret=W3N0K22PWTZLITEKUFCXA5UU0KKTJQNLHS1IOD0NQABZIBF4&v=20180323&section=food&limit=2&near=Chicago, IL&price=1,2
'''
# Params for Query 3
# params = dict(
#   client_id=foursquare_keys[0],
#   client_secret=foursquare_keys[1],
#   v='20180323',
#   near='Chicago, IL',
#   section='food',
#   limit=1,
#   price='1,2'
# )

# fire the request and get the response
resp = requests.get(url=base_url, params=params)
print(resp.status_code)
data = json.loads(resp.text)

# to write the data to an external file, do the following.
# Be sure to store the previous file with a name other than data.json before running this script again
# otherwise older data would be overridden. The data.json file can be found in the same directory as this python file

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)



