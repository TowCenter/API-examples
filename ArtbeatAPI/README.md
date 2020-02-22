# API: NY Art Beat

## About the API
The New York Art Beat website provides information on exhibitions, openings and other art-related events and venues in New York City. Its data is accessible via an API, documented [here](http://www.nyartbeat.com/resources/doc/api). The API is open to use for non-commercial purposes, provided the application don't cause heavy traffic (what is meant by `heavy traffic` is not specified).

The API is open, meaning no `apiKey` or `Oauth` token is necessary, and it uses the `http` protocol. Only `GET` requests are allowed and results are returned in the `XML` format. This guide includes some example on how to work with the returned XML content, but it won't go into the [details](https://www.w3schools.com/xml/default.asp) of the `XML` markup language.

The NY Art Beat API consists of two parts: a series of individual endpoints with lists of events by type, area, etc. Examples These endpoints only accept `GET` requests with no parameters. In addition there is a `event_searchNear` endpoint, which returns events based on location and other parameters. This guide includes examples for both parts.

## Setup

We use `Python 3.7.0` for this guide, although any version of `Python 3` should work. The full code example can be found in `ny_art_beat_api_client.py` in this repo.

We start by importing the Python `requests` and `xml.etree.ElementTree` libary. The former is used to make the `http` request, the latter for parsing the returned `XML` data.

    import requests
    import xml.etree.ElementTree as etree

Set the base_url:

    base_url = 'http://www.nyartbeat.com/list/'


## Examples

### Example 1: Getting a list of free events

We define the endpoint and make the `GET` request to the appropriate endpoint. For a list of endpoints, as well as a description of the structure of the returned `XML` data, check out the `API: events Listing` section in the [API docs](http://www.nyartbeat.com/resources/doc/api), and print the [status code](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html), which should be `200` if the request was successful.

    free_endpoint = 'event_free.en.xml'
    free_url = '{}{}'.format(base_url, free_endpoint)
    response = requests.get(free_url)
    print(response.status_code)

The xml content in the response comes as a string, so it needs to parsed using the `etree` library.

    free_events_string = response.content
    free_events = etree.fromstring(free_events_string)

To illustrate what can be done with the results, here is an example to print out the name and url of all events with the word `abstract` in the description. It makes use of the features of the `etree` [library](https://docs.python.org/3/library/xml.etree.elementtree.html#parsing-xml) and saves the output to a `txt` file using the standard Python [file-handling library](https://www.w3schools.com/python/python_file_handling.asp).

    # customize the query here -- has to be lowercase
    query = 'abstract'

    # this array will store the events matching our simple query
    event_list = []

    # loop over the children of the root element in the xml (see https://docs.python.org/3/library/xml.etree.elementtree.html#parsing-xml)
    for event in free_events:
      description = event.find('Description').text
      # skip over if the Description is empty
      if description is not None and query in description.lower():
        event_info = "{}: {}".format(event.find('Name').text, event.get('href'))
        event_list.append(event_info)

    # save the matching events in a txt file
    filepath = 'events.txt'
    with open(filepath, 'w') as file_handler:
        for item in event_list:
            file_handler.write("{}\n".format(item))

### Examples 2 & 3: Querying based on location

Next, we will use the `event_searchNear` endpoint to search for events near the Columbia University Graduate School of Journalism. We need the longitude and latitude, of the J-school. I got that information manually from Google Maps using Method 3 described [here](https://www.wikihow.com/Get-Latitude-and-Longitude-from-Google-Maps), but it is possible to integrate with another API to get the longitude and latitude using a geocoding API.

Similar to *Example 1*, we define the endpoint


    search_near_endpoint = 'event_searchNear'
    search_near_url = '{}{}'.format(base_url, search_near_endpoint)

This time, we include additional search params: the longitude and latitude as floats, and the search range. Note that the range is described as a string ending with `m` for meters. `3000m` is the max range.

    # using the long & latitude of the J-school address as an example.
    query_params = {
        'latitude': 40.807598,
        'longitude': -73.963600,
        'searchrange': '3000m'
    }
    response = requests.get(search_near_url, params=query_params)
    print(response.url)
    print(response.content)

The url should look like this

    http://www.nyartbeat.com/list/event_searchNear?latitude=40.807598&longitude=-73.9636&searchrange=3000m

Lastly, let's make a more elaborate request by adding additional parameters to the query_params object, we only want to see free events, we limit our results to a max of 5, and we sort the events by the closing data. A full list of query parameters and there potential values can be found in the [API docs](http://www.nyartbeat.com/resources/doc/api).

    query_params['free'] = 1
    query_params['maxresults'] = 5
    query_params['sortorder'] = "closingsoon"


Similar to *Example 1*, we parse the `XML` content of the response:

    response = requests.get(search_near_url, params=query_params)
    events_near_columbia_string = response.content
    events_near_columbia = etree.fromstring(events_near_columbia_string)

To illustrate what can be done with the response, the example code in the `ny_art_beat_api_client.py` file goes on to fetch images from the returned and save them using Python's `PILLOW` image handling library.






