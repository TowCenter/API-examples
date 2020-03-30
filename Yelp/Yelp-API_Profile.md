# Yelp API Profile

[![N|Solid](https://s3-media3.fl.yelpcdn.com/assets/srv0/developer_pages/b2ca299e2633/assets/img/318x90_yelp_fusion.png)](https://www.yelp.com/developers/documentation/v3/get_started)

Yelp is a crowd-sourced business review platform as well as a directory of businesses provided via the Yelp website and mobile app. The Yelp Fusion API is available for usage to developers who want to create their own app, and uses private key authentication to authenticate endpoints. Yelp's Fusion API gives search, data and autocomplete access to information about the 50 million businesses listed on Yelp across its 32 international markets.

For help and information, Yelp provides a [tutorial]( https://www.yelp.com/developers/documentation/v3/get_started), [FAQ](https://www.yelp.com/developers/faq), [documentation](https://www.yelp.com/developers/documentation/v3) and [code samples](https://github.com/Yelp/yelp-fusion#code-samples) for its API. Yelp suggests downloading and using [Postman](https://app.getpostman.com/run-collection/6b506a43109229cb2798) to try the API out for yourself.

There's a limit to daily usage, with a daily API limit of 5000. Under the Manage App page, you can check your API Usage, which lets you know your remaining API calls, 30-day hit total, 30-day daily mean hits and 30-day daily median hits.

> **Sidenote:** You're also given the option to join the Developer Beta. If you join, this means you'll have access to [Yelp's GraphQL API](https://www.yelp.com/developers/graphql/guides/basic_usage), a query language for APIs that gives you flexibility to specify what data you need, allowing you to customize your requests/responses when going through data on Yelp. once you join, the GraphQL API has a daily points limit of 250,000 and also provides a GraphQL Usage section showing daily usage and 30-day usage.

All endpoints branch out from: https://api.yelp.com/v3. Yelp Fusion API's current endpoints aka the different query parameters possible are as follows:

| Endpoint | Description |
| ------ | ------ |
| /businesses/search | Search for businesses by keyword, category, location, price level, etc. |
| /businesses/search/phone | Search for businesses by phone number. |
| /transactions/{transaction_type}/search | Search for businesses which support food delivery transactions. |
| /businesses/{id} | Get rich business data, such as name, address, phone number, photos, Yelp rating, price levels and hours of operation. |
| /businesses/matches | Find the Yelp business that matches an exact input location. Use this to match business data from other sources with Yelp businesses. |
| /businesses/{id}/reviews | Get up to three review excerpts for a business. |
| /autocomplete | Provide autocomplete suggestions for businesses, search keywords and categories. |

#### Set Up

To begin using Yelp Fusion API, follow the steps below to get an API key:

  1. [Create a Yelp user account](https://www.yelp.com/signup)
  2. [Go to the Manage App section](https://www.yelp.com/developers/v3/manage_app)
  3. Create an app with Yelp to receive an API key
 
**🔑 Save your key and keep it safe! 🔑**

Next, download [Postman](https://app.getpostman.com/run-collection/6b506a43109229cb2798) as Yelp suggests.

[![N|Solid](https://i.pinimg.com/originals/6a/9d/0d/6a9d0d462cdc2b0b97e607f32aa124e9.png)](https://www.postman.com/downloads/)

Yelp's authorization method is separate from its connection, so we can't simply plug a URL with our API key into our browser. We need to either use Postman or write our own code. For the sake of this profile, I'll talk you through using Postman and provide query strings for Postman, but feel free to go through Yelp's [code samples](https://github.com/Yelp/yelp-fusion#code-samples) to see how you could use their API with Python, PHP, Node.js, R or Swift. If you have any issues or feedback, create [a new issue on the Github repo linked](https://github.com/Yelp/yelp-fusion).

Once you have Postman downloaded, we can start building an API request to use Yelp Fusion API:

1. Open Postman and click on the arrow next to +New (top left corner), then click on **Request** under Building Blocks. Name your request and put it in a new folder (suggested name "Yelp API Queries" for ease of finding).
2. Underneath the request line that starts with GET, you'll see a bunch of tabs, including an Authorization tab. Click Authorization, then click **Bearer Token** under TYPE. Paste your API Key where it says Token.
3. Switch the tab back to Params. You should see a little green circle next to the Authorization tab. Now you're all good to go and we can start using the GET request line to enter the Yelp API endpoints and make queries! 
 
#### Sample Use Case
A cool example of Yelp Fusion API usage is Katie Hempenius's map visualization of San Francisco based off of the city's ~30,000 Yelp listings. Hempenius used the Yelp API to "identify the category(s) of businesses that are unusually prevalent in each zip code":
[![N|Solid](https://katiehempenius.com/yelp-map-of-san-francisco/sf_yelp_map.png)](https://katiehempenius.com/post/yelp-map-of-san-francisco/)

## It's Query Time
Ok, now that you've seen all the information Yelp provides regarding its API; downloaded and set up Postman; and seen a cool example using the API, it's time to walk through three sample queries together so you can understand how to access specific information yourself.

### 1. Autocomplete

For starters, we'll check out Yelp Fusion API's autocomplete search query. The **/autocomplete** endpoint returns automatically-filled suggestions based on input word(s). If you don't specify location (via latitude and longitude), you'll receive keywords and/or categories. To also get businesses, you need to include latitude and longitude.

The general request looks like this:
```sh
    GET https://api.yelp.com/v3/autocomplete
```

Go ahead and stick the general request into your Postman GET request box.
    
Autocomplete's parameters are:

| Name | Description |
| ------ | ------ |
| text | (Required) input string that autocomplete suggestions are formed from |
| latitude | (Required to include businesses) decimal latitude of location |
| longitude | (Required to include businesses) decimal longitude of location) |
| locale | (Optional) Defaults to en_US, [see list of Yelp locales](https://www.yelp.com/developers/documentation/v3/supported_locales) |

In Postman, under the Params tab, you'll see a section called KEY and a section called VALUE. In KEY you must add "text" and in the VALUE next to it you can put whatever text you want to get an autocomplete suggestion for. For the sake of our example, we'll put acai.

So essentially your search query in Postman should look like this:

| KEY | VALUE |
| ------ | ------ |
| text | acai |

Which autofills your GET request to:
```sh
    GET https://api.yelp.com/v3/autocomplete?text=acai
```

Now press the SEND button, and voila:
```sh
{
    "categories": [
        {
            "alias": "acaibowls",
            "title": "Acai Bowls"
        },
        {
            "alias": "juicebars",
            "title": "Juice Bars & Smoothies"
        },
        {
            "alias": "brazilian",
            "title": "Brazilian"
        }
    ],
    "businesses": [],
    "terms": [
        {
            "text": "Acai"
        },
        {
            "text": "Acai Bowl Near Me"
        },
        {
            "text": "Acai Bowls Open Now"
        }
    ]
}
```

We see that we got categories and terms in response to our query. Our acai search gave us autocomplete suggestions of "acai bowls", "juice bars & smoothies and brazilian" for categories, and to "acai", "acai bowl near me" and "acai bowls open now" for terms. The businesses section is empty ( [] means no terms were returned) since we didn't provide a latitude or longitude. Let's try adding latitude, longitude and locale. For kicks, we'll see what autocompletes when we look for acai in London, UK. London's latitude is **51.5074** and its longitude is **0.1278**. Its locale is **en_GB**. Remember to include the locale if the latitude/longitude you're searching is NOT in good ol' USA, because the Yelp API has it so that locale defaults to US if no locale parameter is provided, which would give us empty search results. [See the list of available Yelp locales you can choose from.](https://www.yelp.com/developers/documentation/v3/supported_locales)

Now our KEY and VALUE sections should look like this:

| KEY | VALUE |
| ------ | ------ |
| text | acai |
| latitude | 51.5074 |
| longitude | 0.1278 |
| locale | en_GB |

Which sets our GET request to:
```sh
    GET https://api.yelp.com/v3/autocomplete?text=acai&latitude=51.5074&longitude=0.1278&locale=en_GB
```
Press SEND, and voila:
```sh
{
    "categories": [
        {
            "alias": "acaibowls",
            "title": "Acai Bowls"
        },
        {
            "alias": "beautysvc",
            "title": "Beauty & Spas"
        },
        {
            "alias": "food",
            "title": "Food"
        }
    ],
    "businesses": [
        {
            "id": "_SHERl2o-Ur_cPEqNZO4iw",
            "name": "acai berry optimum"
        }
    ],
    "terms": [
        {
            "text": "Acai"
        },
        {
            "text": "Best Acai Bowls"
        },
        {
            "text": "Activities"
        }
    ]
}
```

Now we see that not only do we get a business, but our categories and terms changed! This means that the autocompleted suggestions in London, UK are different from the autocompleted suggestions in the United States. Practically speaking, this means that when a Yelp user types "acai" into the search bar on their Yelp app, the suggested autocomplete words are location-dependent. In London, UK, we'd get "acai bowls", "beauty & spas" and "food" as our suggested categories, and "acai", "best acai bowls" and "activities" as our suggested terms. We also now see a business, with the unique ID its stored under in Yelp and its real-life name: Acai Berry Optimum.

A quick Google search shows us that [Acai Berry Optimum](https://www.yelp.com/biz/acai-berry-optimum-london) is indeed a real business in London labeled under "Beauty & Spas" and "Health Markets" categories.

### 2. Phone Search

Now on to our second sample query search, **/businesses/search/phone**, where putting in a phone number returns a list of any business(es) with said phone number. But wait, you ask, how can there be multiple businesses with the same phone number? It's possible: chain stores might have the same +1 800 number and also it might be useful to simply reverse search from a phone number. For example, say you get a phone call from an unknown number and want to see if its from a business. A caveat, though, is that the Yelp Fusion API doesn't return businesses with no reviews, which does limit the data.

Now down to business *badumtish. The general request is:
```sh
    GET https://api.yelp.com/v3/businesses/search/phone
```
Go ahead and stick the general request above into your Postman GET request line.

The parameters for phone search are:

| Name | Description |
| ------ | ------ |
| phone | (Required) A phone number starting with the country code and in the format +12345678, for example |
| locale | (Optional) Set where you want to localize results to, defaults to en_US. [See list of Yelp locales.](https://www.yelp.com/developers/documentation/v3/supported_locales) |

We're going to stick with our "acai" theme here, so I looked up "acai" on Google Maps from my current location (Columbia University Graduate School of Journalism). One result that pops up is Fruces Juice Bar, with a phone number of (646) 861-3279, meaning we would format it under VALUE as +16468613279.

So under Params -> Query Params -> KEY we would put "phone", and in VALUE (next to KEY) we would put +16468613279.

Your Postman screen should look like the below:

| KEY | VALUE |
| ------ | ------ |
| phone | +16468613279 |

Making your GET request automatically populate to:
```sh
    GET https://api.yelp.com/v3/businesses/search/phone?phone=+16468613279
 ```
Press SEND and lo and behold:
```sh
{
    "businesses": [
        {
            "id": "BIsgBK_aQUbvAndI_LbprA",
            "alias": "fruces-new-york-2",
            "name": "Fruces",
            "image_url": "https://s3-media0.fl.yelpcdn.com/bphoto/JXnh5syhAMQPg3jhkc30dQ/o.jpg",
            "is_closed": false,
            "url": "https://www.yelp.com/biz/fruces-new-york-2?adjust_creative=9Ufyj7pqQkQcWhP9LaaKgw&utm_campaign=yelp_api_v3&utm_medium=api_v3_phone_search&utm_source=9Ufyj7pqQkQcWhP9LaaKgw",
            "review_count": 28,
            "categories": [
                {
                    "alias": "juicebars",
                    "title": "Juice Bars & Smoothies"
                }
            ],
            "rating": 5.0,
            "coordinates": {
                "latitude": 40.818237,
                "longitude": -73.9531219
            },
            "transactions": [
                "pickup",
                "delivery"
            ],
            "price": "$",
            "location": {
                "address1": "1496 Amsterdam Ave",
                "address2": "",
                "address3": "",
                "city": "New York",
                "zip_code": "10031",
                "country": "US",
                "state": "NY",
                "display_address": [
                    "1496 Amsterdam Ave",
                    "New York, NY 10031"
                ]
            },
            "phone": "+16468613279",
            "display_phone": "(646) 861-3279"
        }
    ],
    "total": 1
}
```

Sure enough, we got Fruces! We see from the bottom of the code produced that there's a total of 1 business with this phone number. The API result even gives us an image url and a url to Fruce's Yelp page (image shown below, click on the image to go to the url our API search provided):

[![N|Solid](https://s3-media0.fl.yelpcdn.com/bphoto/JXnh5syhAMQPg3jhkc30dQ/o.jpg)](https://www.yelp.com/biz/fruces-new-york-2?adjust_creative=9Ufyj7pqQkQcWhP9LaaKgw&utm_campaign=yelp_api_v3&utm_medium=api_v3_phone_search&utm_source=9Ufyj7pqQkQcWhP9LaaKgw)

Yum, acai! Now let's parse out the rest of the data we found into plain human words:

| Category | Value |
| ------ | ------ |
| Is Closed | False (aka Fruces is open) |
| Review Count | 28 reviews |
| Categories | Juice Bars & Smoothies |
| Rating | 5.0 (out of 5.0) |
| Coordinates | 40.818237, -73.9531219 |
| Transactions | Pickup, Delivery |
| Price | $ (lowest price range on Yelp) |
| Address | 1496 Amsterdam Ave, New York, NY 10031, US |

Nice work! Now for our third and final sample query search...

### 3. Transaction Search

For our third search, we'll be trying out Yelp Fusion API's **/transactions/{transaction_type}/search**. This search returns businesses that offer food delivery. Same caveat as with the phone number search: the Yelp Fusion API doesn't return businesses without reviews. Also the only transaction type that's valid right now is "delivery". Also ALSO this endpoint only works within the US aka locale en_US and nowhere else. Hopefully Yelp will expand on this endpoint functionality.

While Yelp provides the general GET request and has it as:
```sh
GET https://api.yelp.com/v3/transactions/{transaction_type}/search
```
A more accurate general GET request would be:
```sh
GET https://api.yelp.com/v3/transactions/delivery/search
```
Go ahead and stick this general request line into your Postman GET request box.

Parameters for transaction search are:

| Name | Description |
| ------ | ------ |
| latitude | (Required when no location is given) decimal latitude of location |
| longitude | (Required when no location is given) decimal longitude of location |
| location | (Required when no latitude and longitude are given) address of where you want your food delivered to |

Let's say I want food delivered to the Columbia University Graduate School of Journalism because I'm working on this API profile and I'm starting to get hungry from all the acai searches.

Write "location" under KEY under the Params tab, and write "Columbia University Graduate School of Journalism NYC" under VALUE. Your Postman should look something like this:

| KEY | VALUE |
| ------ | ------ |
| location | Columbia University Graduate School of Journalism NYC |

Your GET request link should now look like this:
```sh
https://api.yelp.com/v3/transactions/delivery/search?location=columbia university graduate school of journalism nyc
```
You know the drill. Press SEND and woah! A whole bunch of data spits out. Scroll to the very bottom (I won't copy and paste that huge block here) to see the total number of businesses that deliver food to Columbia University Graduate School of Journalism. As of the day I search this, 7 February 2020, there are 92 total businesses.

I'll pick a random one so that you can see what sort of data you're getting from this search.

Let's take a look at Famous Famiglia Pizzeria. Similar to the phone number search, we get a singular image url and the business's Yelp url. See the API-provided image below and click to go to the provided Yelp url:

[![N|Solid](https://s3-media3.fl.yelpcdn.com/bphoto/72zL4RRdIQ_-zIHH55xXpQ/o.jpg)](https://www.yelp.com/biz/famous-famiglia-pizzeria-new-york-9?adjust_creative=9Ufyj7pqQkQcWhP9LaaKgw&utm_campaign=yelp_api_v3&utm_medium=api_v3_transactions_search_delivery&utm_source=9Ufyj7pqQkQcWhP9LaaKgw)

Wow... someone found a screw on top of their pizza slice, yum. Don't you just hate when that happens to your pizza? When I go to the Yelp URL provided for the business, the screw pizza above is the most recent image uploaded, so it seems Yelp Fusion API returns an image URL simply to the most recent image at the time of search. So as of 7 February 2020, screw pizza pops up for Famous Famiglia Pizzeria.

Other data, parsed in readable human form:

| Category | Value |
| ------ | ------ |
| Is Closed | False (aka Famous Famiglia Pizzeria is open) |
| Review Count | 82 |
| Categories | Italian, Pizza |
| Rating | 3.0 (out of 5.0) |
| Coordinates | 40.8047916, -73.9665391 |
| Transactions | Pickup, Delivery |
| Price | $ (lowest price range on Yelp) |
| Address | 2859 Broadway, New York, NY 10025, US |

### Thank you for joining me on this delicious journey through the Yelp Fusion API!
