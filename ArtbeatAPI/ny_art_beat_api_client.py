import requests
import re
import xml.etree.ElementTree as etree
from PIL import Image


base_url = 'http://www.nyartbeat.com/list/'

# example 1
#sends out a GET request to obtain an xml file with free events and filter based on the query
def  get_free_events(query):

  free_endpoint = 'event_free.en.xml'
  free_url = '{}{}'.format(base_url, free_endpoint)
  response = requests.get(free_url)

  print("Response status is {}".format(response.status_code))

  free_events_string = response.content

  # the xml content in the response comes as a string, so it needs to parsed
  free_events = etree.fromstring(free_events_string)

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


# example 2 - simple call
def events_near_simple(query_params):
  search_near_endpoint = 'event_searchNear'
  search_near_url = '{}{}'.format(base_url, search_near_endpoint)
  # using the long & latitude of the J-school address as an example.

  response = requests.get(search_near_url, params=query_params)
  print(response.url)
  print("Response status is {}".format(response.status_code))
# example 3 - more elaborate query (still near Columbia) + get the first image for each event

# add additional query params to the query_params
def events_near_complex(query_params):
  search_near_endpoint = 'event_searchNear'
  search_near_url = '{}{}'.format(base_url, search_near_endpoint)

  response = requests.get(search_near_url, params=query_params)
  print("Response status is {}".format(response.status_code))
  events_near_columbia_string = response.content

  # the xml content in the response comes as a string, so it needs to parsed
  events_near_columbia = etree.fromstring(events_near_columbia_string)

  # filter out the events without pictures, which uses this url as a dummy
  nopic = 'http://www.nyartbeat.com/resources/images/nopic'


  # helper method to the names to save the images: https://stackoverflow.com/questions/295135/turn-a-string-into-a-valid-filename
  def get_valid_filename(s):
      s = str(s).strip().replace(' ', '_')
      return re.sub(r'(?u)[^-\w.]', '', s)

  for event in events_near_columbia:
    event_name = event.find('Name').text
    image_element = event.find('Image')
    if image_element is not None:
      image_url = image_element.get('src')
      if not nopic in image_url:
        # Dowonload and save image: https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
        img = Image.open(requests.get(image_url, stream=True).raw)
        img.save(get_valid_filename("{}.jpg".format(event_name)))


print("For each request, status 200 means the request was successful, 4xx means something went wrong")

print("Example 1:")
print("This example creates a file called 'events.txt'")
query = 'abstract'
get_free_events(query)

print("Example 2:")
print("This example prints the request url and response status to the console")
query_params = {
    'latitude': 40.807598,
    'longitude': -73.963600,
    'searchrange': '3000m'
}
events_near_simple(query_params)

print("Example 3:")
print("This example downloads the first image for the five free events closing soon in a 3000m radius around the Journalism school")
query_params['free'] = 1
query_params['maxresults'] = 5
query_params['sortorder'] = "closingsoon"
events_near_complex(query_params)
