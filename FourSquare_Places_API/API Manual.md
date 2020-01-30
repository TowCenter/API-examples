# FourSquare Places API Manual:

The Places API from FourSquare provides search results for venues, recommended venues, venue photos, tips, hours, menu, list of trending venues, access information on current events at a venue and a host of other options. It also allows to report errors about venues. All these options have their own endpoints. For example, to get details of a venue, we can use the following endpoint:

`https://api.foursquare.com/v2/venues/VENUE_ID`

And for the list of venues near the current location, we use the following endpoint:

`https://api.foursquare.com/v2/venues/search`

For the purposes of this exercise, I chose to document Get Venue Recommendations . It has the following endpoint:

`https://api.foursquare.com/v2/venues/explore`

Structure of the full URL is as follows:

`https://api.foursquare.com/v2/venues/explore?client_id=<CLIENT_ID>&client_secret=<CLIENT_SECURE_KEY>&v=<VERSION>&{ll=<LATITUDE, LONGITUDE> OR near=<CITY/STATE/AREA>}`


The above URL structure specifies all the mandatory parameters that are required for the API to work and return data. Using this API requires two keys: Client ID and Client Secure. Here are the steps to obtain the keys.

* Create a developer account on https://developer.foursquare.com 
* Create an app which shall use the FourSquare Places API. Provide a name for the app and the URL. If URL is not known, put in a random URL. I put in journalism.columbia.edu
* Select a payment plan. Depending on whether you need premium features or not, select the plan which is most appropriate for your needs.
* Once the app is created and payment plan is chosen, the app appears on the profile page, along with the required keys.

A sample query in Python is as follows:

```
import json, requests
url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
  client_id='CLIENT_ID', # replace with your key
  client_secret='CLIENT_SECRET', # replace with your key
  v='20180323',
  ll='40.7243,-74.0018',
  query='coffee',
  limit=1
)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
```

The above code was taken from [https://developer.foursquare.com/docs/api](https://developer.foursquare.com/docs/api).

Client ID and Client Secure are needed for Userless authentication. For User authentication, FourSquare uses OAuth 2.0. In this document, we focus on userless authentication.

The parameters are explained below:
1.	Client ID and Client Secure: Authentication keys for the API request.
2.	v: Version. This is also a mandatory parameter. I used the version value given in the sample setup code
3.	ll: Latitude and longitude. This key is required unless ‘near’ is specified
4.	near: City/state/area. Examples include ‘New York, NY’ or ‘Chicago’ or ‘Manhattan’. It is advisable to use a specific location like ‘Manhattan’ or ‘West Village’ rather than just the state to get better results.
5.	section: This parameter can take the following values:
    *	food
    *	drinks
    *	coffee
    *	shops
    *	arts
    *	outdoor
    *	sights
    *	trending
    *	nextVenues (venues frequently visited after a given venue)
    *	topPicks (this option generates a mix of recommendations if nothing is specified in the query parameter)
6.	query: Something that can searched against a venue’s category. This parameter has no effect when section is specified
7.	limit: number of results to be returned. Maximum no. of results that can be returned is 50
8.	offset: used for pagination of results. Maximum limit is 50
9.	llAcc: Accuracy of the latitude and longitude in meters
10.	alt: Altitude of user’s location, in meters
11.	radius: to search within the specified radius, in meters. This parameter is not required, a radius is chosen based on density of venues in the area. Maximum value of radius is 100,000 meters
12.	novelty: allowed values for this parameter are new and old. It is used to filter results based on whether the user has already been to these places or not. If this parameter is absent, results will include both new and old venues.
13.	friendVisits: Allowed values for this parameter are visited and notVisited. It filters results based on whether the user’s friends have visited the venue or not.
14.	time: Allowed value for this parameter is any. By default, the API returns results based on current time of day.
15.	day: Allowed value for this parameter is any. By default, the API returns results based on current day of the week.
16.	lastVenue: This parameter specifies a venue ID and is used to return venues which users visit frequently after visiting a certain venue. It is used in combination with the intent=nextVenues parameter
17.	openNow: Takes value 1 to indicate results should include only those venues which are open at that time. 
18.	sortByDistance: Takes value 1 to sort the venues in order of distance
19.	price: Specifies price points. It can take comma separated values. Values can range from 1 to 4 in the following format: ‘2,4’. The price bands are defined as follows:
    1. less than $10 per entrée
    2. $10 - $20 per entrée
	3. $20 - $30 per entrée
	4. greater than $30 per entrée
20.	saved: This parameter is used to get only those venues which the user has saved on their to-do list.

Let’s discuss the different queries that can be formed using the query parameters mentioned above. As mentioned earlier, client_id, client_secret and v are mandatory, so they have to be passed in every query.

## Query 1

https://api.foursquare.com/v2/venues/explore?client_id=04JOGOUXDKSCL2LDGHWILZDZXB0YUF5Q5NVOQ0CS2FFH3H2D&client_secret=W3N0K22PWTZLITEKUFCXA5UU0KKTJQNLHS1IOD0NQABZIBF4&v=20180323&query=wine&limit=1&near=New%20York,%20NY

The above query utilizes the following query parameters:
1.	query
2.	limit
3.	near

The query can be constructed as follows:
```
import json, requests
from foursquarekeys import foursquare_keys

# This is the base URL
base_url = 'https://api.foursquare.com/v2/venues/explore'
params = dict(
  client_id=foursquare_keys[0],
  client_secret=foursquare_keys[1],
  v='20180323',
  near='New York, NY',
  query='wine',
  limit=1
)

# fire the request and receive response
resp = requests.get(url=base_url, params=params)
# get the text data received in the response`
data = json.loads(resp.text)

# to write the data to an external file, do the following.
# Be sure to store the previous file with a name other than data.json before running this script again
# otherwise older data would be overridden. The data.json file can be found in the same directory as this python file

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)
```

The response for this query is given below:

```
{
    "meta": {
        "code": 200,
        "requestId": "5c5e56e04434b95ecf22ed79"
    },
    "response": {
        "suggestedFilters": {
            "header": "Tap to show:",
            "filters": [
                {
                    "name": "With specials",
                    "key": "specials"
                },
                {
                    "name": "Open now",
                    "key": "openNow"
                }
            ]
        },
        "geocode": {
            "what": "",
            "where": "new york ny",
            "center": {
                "lat": 40.742185,
                "lng": -73.992602
            },
            "displayString": "New York, NY, United States",
            "cc": "US",
            "geometry": {
                "bounds": {
                    "ne": {
                        "lat": 40.882214,
                        "lng": -73.907
                    },
                    "sw": {
                        "lat": 40.679548,
                        "lng": -74.047285
                    }
                }
            },
            "slug": "new-york-city-new-york",
            "longId": "72057594043056517"
        },
        "warning": {
            "text": "There aren't a lot of results for \"wine.\" Try something more general, reset your filters, or expand the search area."
        },
        "headerLocation": "New York",
        "headerFullLocation": "New York",
        "headerLocationGranularity": "city",
        "query": "wine",
        "totalResults": 378,
        "suggestedBounds": {
            "ne": {
                "lat": 40.735099334914345,
                "lng": -73.98948557711682
            },
            "sw": {
                "lat": 40.732399675128896,
                "lng": -73.98677040218448
            }
        },
        "groups": [
            {
                "type": "Recommended Places",
                "name": "recommended",
                "items": [
                    {
                        "reasons": {
                            "count": 0,
                            "items": [
                                {
                                    "summary": "This spot is popular",
                                    "type": "general",
                                    "reasonName": "globalInteractionReason"
                                }
                            ]
                        },
                        "venue": {
                            "id": "4a319883f964a520fc991fe3",
                            "name": "Trader Joe's Wine Shop",
                            "contact": {},
                            "location": {
                                "address": "138 E 14th St",
                                "crossStreet": "btwn Irving Pl & 3rd Ave",
                                "lat": 40.73374950502162,
                                "lng": -73.98812798965065,
                                "labeledLatLngs": [
                                    {
                                        "label": "display",
                                        "lat": 40.73374950502162,
                                        "lng": -73.98812798965065
                                    }
                                ],
                                "postalCode": "10003",
                                "cc": "US",
                                "city": "New York",
                                "state": "NY",
                                "country": "United States",
                                "formattedAddress": [
                                    "138 E 14th St (btwn Irving Pl & 3rd Ave)",
                                    "New York, NY 10003",
                                    "United States"
                                ]
                            },
                            "categories": [
                                {
                                    "id": "4bf58dd8d48988d119951735",
                                    "name": "Wine Shop",
                                    "pluralName": "Wine Shops",
                                    "shortName": "Wine Shop",
                                    "icon": {
                                        "prefix": "https://ss3.4sqi.net/img/categories_v2/shops/food_wineshop_",
                                        "suffix": ".png"
                                    },
                                    "primary": true
                                }
                            ],
                            "verified": true,
                            "stats": {
                                "tipCount": 0,
                                "usersCount": 0,
                                "checkinsCount": 0,
                                "visitsCount": 0
                            },
                            "beenHere": {
                                "count": 0,
                                "lastCheckinExpiredAt": 0,
                                "marked": false,
                                "unconfirmedCount": 0
                            },
                            "photos": {
                                "count": 0,
                                "groups": []
                            },
                            "hereNow": {
                                "count": 0,
                                "summary": "Nobody here",
                                "groups": []
                            }
                        },
                        "referralId": "e-0-4a319883f964a520fc991fe3-0"
                    }
                ]
            }
        ]
    }
}
```

## Query 2

https://api.foursquare.com/v2/venues/explore?client_id=04JOGOUXDKSCL2LDGHWILZDZXB0YUF5Q5NVOQ0CS2FFH3H2D&client_secret=W3N0K22PWTZLITEKUFCXA5UU0KKTJQNLHS1IOD0NQABZIBF4&v=20180323&section=sights&limit=1&ll=40.716558,-74.004608

The above query utilizes the following parameters:
1.	section
2.	ll
3.	limit

Section has been set to sights. The value for _section_ drives the search results in this case.

The query can be constructed as follows:
```
import json, requests
from foursquarekeys import foursquare_keys

# This is the base URL
base_url = 'https://api.foursquare.com/v2/venues/explore'
params = dict(
  client_id=foursquare_keys[0],
  client_secret=foursquare_keys[1],
  v='20180323',
  ll='40.716558,-74.004608',
  section='sights',
  limit=1
)

# fire the request and receive response
resp = requests.get(url=base_url, params=params)
# get the text data received in the response`
data = json.loads(resp.text)

# to write the data to an external file, do the following.
# Be sure to store the previous file with a name other than data.json before running this script again
# otherwise older data would be overridden. The data.json file can be found in the same directory as this python file

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)
```


The response for this query is given below:

```
{
    "meta": {
        "code": 200,
        "requestId": "5c5e59daf594df7dc896a297"
    },
    "response": {
        "suggestedFilters": {
            "header": "Tap to show:",
            "filters": [
                {
                    "name": "$-$$$$",
                    "key": "price"
                },
                {
                    "name": "With specials",
                    "key": "specials"
                }
            ]
        },
        "warning": {
            "text": "There aren't a lot of results near you. Try something more general, reset your filters, or expand the search area."
        },
        "suggestedRadius": 600,
        "headerLocation": "Tribeca",
        "headerFullLocation": "Tribeca, New York",
        "headerLocationGranularity": "neighborhood",
        "totalResults": 229,
        "suggestedBounds": {
            "ne": {
                "lat": 40.71949124153396,
                "lng": -74.00630124446423
            },
            "sw": {
                "lat": 40.71679158174851,
                "lng": -74.00358118023269
            }
        },
        "groups": [
            {
                "type": "Recommended Places",
                "name": "recommended",
                "items": [
                    {
                        "reasons": {
                            "count": 0,
                            "items": [
                                {
                                    "summary": "This spot is popular",
                                    "type": "general",
                                    "reasonName": "globalInteractionReason"
                                }
                            ]
                        },
                        "venue": {
                            "id": "4fbbd9ede4b0756c0d4c2364",
                            "name": "Aire Ancient Baths",
                            "contact": {},
                            "location": {
                                "address": "88 Franklin St",
                                "crossStreet": "at Church St",
                                "lat": 40.718141411641234,
                                "lng": -74.00494121234846,
                                "labeledLatLngs": [
                                    {
                                        "label": "display",
                                        "lat": 40.718141411641234,
                                        "lng": -74.00494121234846
                                    }
                                ],
                                "distance": 178,
                                "postalCode": "10013",
                                "cc": "US",
                                "city": "New York",
                                "state": "NY",
                                "country": "United States",
                                "formattedAddress": [
                                    "88 Franklin St (at Church St)",
                                    "New York, NY 10013",
                                    "United States"
                                ]
                            },
                            "categories": [
                                {
                                    "id": "4bf58dd8d48988d1ed941735",
                                    "name": "Spa",
                                    "pluralName": "Spas",
                                    "shortName": "Spa",
                                    "icon": {
                                        "prefix": "https://ss3.4sqi.net/img/categories_v2/shops/spa_",
                                        "suffix": ".png"
                                    },
                                    "primary": true
                                }
                            ],
                            "verified": true,
                            "stats": {
                                "tipCount": 0,
                                "usersCount": 0,
                                "checkinsCount": 0,
                                "visitsCount": 0
                            },
                            "beenHere": {
                                "count": 0,
                                "lastCheckinExpiredAt": 0,
                                "marked": false,
                                "unconfirmedCount": 0
                            },
                            "photos": {
                                "count": 0,
                                "groups": []
                            },
                            "venuePage": {
                                "id": "191281001"
                            },
                            "hereNow": {
                                "count": 0,
                                "summary": "Nobody here",
                                "groups": []
                            }
                        },
                        "referralId": "e-10-4fbbd9ede4b0756c0d4c2364-0"
                    }
                ]
            }
        ]
    }
}

```

## Query 3

https://api.foursquare.com/v2/venues/explore?client_id=04JOGOUXDKSCL2LDGHWILZDZXB0YUF5Q5NVOQ0CS2FFH3H2D&client_secret=W3N0K22PWTZLITEKUFCXA5UU0KKTJQNLHS1IOD0NQABZIBF4&v=20180323&section=food&limit=2&near=Chicago,%20IL&price=1,2

The above query fetches food venues near Chicago. It utilizes the following parameters:
1.	section
2.	near
3.	price

The query can be constructed as follows:
```
import json, requests
from foursquarekeys import foursquare_keys

# This is the base URL
base_url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
  client_id=foursquare_keys[0],
  client_secret=foursquare_keys[1],
  v='20180323',
  near='Chicago, IL',
  section='food',
  limit=1,
  price='1,2'
)

# fire the request and receive response
resp = requests.get(url=base_url, params=params)
# get the text data received in the response`
data = json.loads(resp.text)

# to write the data to an external file, do the following.
# Be sure to store the previous file with a name other than data.json before running this script again
# otherwise older data would be overridden. The data.json file can be found in the same directory as this python file

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)
```

Response for the above query is given below:
```
{
  "meta": {
    "code": 200, 
    "requestId": "5c6097a7db04f54530cf1bdd"
  }, 
  "response": {
    "headerFullLocation": "Chicago", 
    "groups": [
      {
        "items": [
          {
            "reasons": {
              "count": 0, 
              "items": [
                {
                  "reasonName": "globalInteractionReason", 
                  "type": "general", 
                  "summary": "This spot is popular"
                }
              ]
            }, 
            "venue": {
              "verified": false, 
              "name": "Publican Quality Meats", 
              "hereNow": {
                "count": 0, 
                "groups": [], 
                "summary": "Nobody here"
              }, 
              "delivery": {
                "url": "https://www.grubhub.com/restaurant/publican-quality-meats-825-w-fulton-market-chicago/758352?affiliate=1131&utm_source=foursquare-affiliate-network&utm_medium=affiliate&utm_campaign=1131&utm_content=758352", 
                "id": "758352", 
                "provider": {
                  "name": "grubhub", 
                  "icon": {
                    "prefix": "https://fastly.4sqi.net/img/general/cap/", 
                    "name": "/delivery_provider_grubhub_20180129.png", 
                    "sizes": [
                      40, 
                      50
                    ]
                  }
                }
              }, 
              "photos": {
                "count": 0, 
                "groups": []
              }, 
              "contact": {}, 
              "location": {
                "city": "Chicago", 
                "labeledLatLngs": [
                  {
                    "lat": 41.886641964097095, 
                    "lng": -87.64871823183745, 
                    "label": "display"
                  }
                ], 
                "cc": "US", 
                "country": "United States", 
                "postalCode": "60607", 
                "state": "IL", 
                "formattedAddress": [
                  "825 W Fulton Market (at Green)", 
                  "Chicago, IL 60607", 
                  "United States"
                ], 
                "crossStreet": "at Green", 
                "address": "825 W Fulton Market", 
                "lat": 41.886641964097095, 
                "lng": -87.64871823183745
              }, 
              "beenHere": {
                "count": 0, 
                "unconfirmedCount": 0, 
                "marked": false, 
                "lastCheckinExpiredAt": 0
              }, 
              "stats": {
                "checkinsCount": 0, 
                "tipCount": 0, 
                "visitsCount": 0, 
                "usersCount": 0
              }, 
              "id": "4f2a0d0ae4b0837d0c4c2bc3", 
              "categories": [
                {
                  "pluralName": "Delis / Bodegas", 
                  "primary": true, 
                  "name": "Deli / Bodega", 
                  "shortName": "Deli / Bodega", 
                  "id": "4bf58dd8d48988d146941735", 
                  "icon": {
                    "prefix": "https://ss3.4sqi.net/img/categories_v2/food/deli_", 
                    "suffix": ".png"
                  }
                }
              ]
            }, 
            "referralId": "e-3-4f2a0d0ae4b0837d0c4c2bc3-0"
          }
        ], 
        "type": "Recommended Places", 
        "name": "recommended"
      }
    ], 
    "totalResults": 190, 
    "warning": {
      "text": "There aren't a lot of results near you. Try something more general, reset your filters, or expand the search area."
    }, 
    "geocode": {
      "what": "", 
      "center": {
        "lat": 41.85003, 
        "lng": -87.65005
      }, 
      "longId": "72057594042815334", 
      "cc": "US", 
      "geometry": {
        "bounds": {
          "sw": {
            "lat": 41.644286, 
            "lng": -87.940101
          }, 
          "ne": {
            "lat": 42.023134999999996, 
            "lng": -87.52366099999999
          }
        }
      }, 
      "displayString": "Chicago, IL, United States", 
      "where": "chicago il", 
      "slug": "chicago-illinois"
    }, 
    "suggestedFilters": {
      "header": "Tap to show:", 
      "filters": [
        {
          "name": "Open now", 
          "key": "openNow"
        }
      ]
    }, 
    "query": "food", 
    "headerLocationGranularity": "city", 
    "headerLocation": "Chicago", 
    "suggestedBounds": {
      "sw": {
        "lat": 41.88529213420437, 
        "lng": -87.64602444917091
      }, 
      "ne": {
        "lat": 41.88799179398982, 
        "lng": -87.65141201450399
      }
    }
  }
}
```
Important fields in response are explained below:
* warning: Mentions a warning message if the filters in the query don’t produce enough results
* groups: An array representing groups of recommendations
* suggestedRadius: This is received in the response if radius is not specified in the query
* headerLocation: Name of the location searched by the user
* headerFullLocation: Full name of the location searched by the user
* id: An ID that uniquely identifies the venue
* name: Best known name for the venue
* location:  Address of the venue. The address could be mentioned in full, or it can be partial. For some venues, the address is hidden for privacy purposes.
* categories: List of categories applied to that venue. 


## Error messages

In case client_id and client_secure are not mentioned, the following response is received:

```
{
    "meta": {
        "code": 400,
        "errorType": "invalid_auth",
        "errorDetail": "Missing access credentials. See https://developer.foursquare.com/docs/api/configuration/authentication for details.",
        "requestId": "5c5e64824c1f6764cf0a124e"
    },
    "response": {}
}
```

In case version is missing from the query, the following error log is received in response:

```
{
    "meta": {
        "code": 410,
        "errorType": "param_error",
        "errorDetail": "The Foursquare API no longer supports requests that do not pass in a version parameter. For more details see https://developer.foursquare.com/overview/versioning",
        "requestId": "5c5e64b16a60712d36a582d8"
    },
    "response": {}
}
```

If both ‘ll’ and ‘near’ are missing from the query, the following error log is received:

```
{
    "meta": {
        "code": 400,
        "errorType": "param_error",
        "errorDetail": "Must provide parameters (ll and radius) or (sw and ne) or (near and radius) or (nearVenueId and ll) or (superVenueId) or (polygon)",
        "requestId": "5c5e64ec1ed2192b5a8afa73"
    },
    "response": {}
}
```

If latitude and longitude specified in ‘ll’ are invalid, then the following response is received:
```
{
    "meta": {
        "code": 400,
        "errorType": "param_error",
        "errorDetail": "Invalid geo coordinates (145.000000,0.000000)",
        "requestId": "5c5e651b351e3d194fae250a"
    },
    "response": {}
}
```

## Query limits

A total of 99,500 queries per day can be made to the Get Venue Recommendations endpoint of the Places API using a free account. For premium users, there is no limit to the number of calls they can make.


## Official documenation

The official documentation of the API can be found at:

https://developer.foursquare.com/docs/api/venues/explore
