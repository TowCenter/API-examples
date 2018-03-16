
This tutorial will use HTTP requests, Python 3, and the urllib python library, which should come preinstalled with Python 3.  

# 1.) First steps

NYC Open data has 1000’s of datasets available to browse and search here: https://opendata.cityofnewyork.us/. Many of them are updated monthly or daily.

Most of the datasets are accessable via the SODA framework. Once you've found a dataset that interests you, by searching it in NYC Open Data, click on the link to its site, and press the 'API' dropdown in the top right corner. You should see 'SODA' listed in the options. 

For this example, we will be using the dataset [Recycling Diversion and Capture Rates](https://data.cityofnewyork.us/Environment/Recycling-Diversion-and-Capture-Rates/gaq9-z3hz). Its SODA documentation can be found [here.](https://dev.socrata.com/foundry/data.cityofnewyork.us/kuz6-hiwt) 

# 2.) Endpoint and App Token

This site should specifiy the API endpoint, which in this case is: https://data.cityofnewyork.us/resource/kuz6-hiwt.json You should also be able to download an app token here. Press "Sign up for an app token!" and follow the steps to create an account. When done, press 'Your Applications', and fill out the form.

From here, navigate to 'App Tokens' on the left hand side, to download your App Token and Secret Token. You can specify the response type by changing in the URL suffix. We will use JSON in this example.

Available reponse types:
* JSON
* XML
* CSV 


```python
# Insert your tokens here
app_token = "your_app_token"
secret_token = "your_secret_token"

# Insert your own API endpoint here
api_endpoint = "https://data.cityofnewyork.us/resource/kuz6-hiwt.json"
```

# 3.) Fetching the entire dataset

Communication on SODA is done via HTTPS.

You have the option of retrieving the entire dataset, and manually parsing it as we show here, or only querying for specific fields as will be demonstrated further down. 


```python
try:
    from urllib.request import Request, urlopen  # Python 3 import
except ImportError:
    from urllib2 import Request, urlopen  # Python 2 import
    
# Create a url string
request_url = ""

# Replace this url with the url provided in your own dataset
request_url += api_endpoint

# Optional add other queries here (see step 5)
request_url += "" # ...

def make_request(url):
    # Construct the request
    req = Request(url)

    # Add your app token as a header to the request 
    # Note: App tokens are not required for public data sets
    req.add_header('X-App-Token', app_token)

    # Make the request
    response = urlopen(req)
    json_response = response.read().decode('utf-8')
    code = response.getcode()
    
    return json_response, code

# Call request function
json_response, code = make_request(request_url)

print('Response ' + str(code))
```

    Response 200


# 4.) Parse recieved data manually with Python

You can now intereact with JSON objects as Python dictionaries:


```python
import json

# Parse the response with the json library
parsed_json = json.loads(json_response)

# Iterate through first 10 objects
for json_obj in parsed_json[:15]:    
    # Display object
    # print(str(json_obj), '\n')
    
    # Replace with your dataset's own features
    feature_1 = '_zone'
    feature_2 = 'capture_rate_mgp_total_mgp_max_mgp_'
    print("Zone:", json_obj[feature_1], '\t', "Capture_Rate:", json_obj[feature_2])
```

    Zone: Manhattan 	 Capture_Rate: 70.18897504989712
    Zone: Manhattan 	 Capture_Rate: 78.96740781007655
    Zone: Manhattan 	 Capture_Rate: 39.4573747627649
    Zone: Manhattan 	 Capture_Rate: 72.95261708509696
    Zone: Manhattan 	 Capture_Rate: 66.60389097792556
    Zone: Manhattan 	 Capture_Rate: 75.99028254954865
    Zone: Manhattan 	 Capture_Rate: 65.57694753203836
    Zone: Manhattan 	 Capture_Rate: 64.84051678971925
    Zone: Manhattan 	 Capture_Rate: 36.0796750024943
    Zone: Manhattan 	 Capture_Rate: 27.431499457387808
    Zone: Manhattan 	 Capture_Rate: 23.51529215573911
    Zone: Manhattan 	 Capture_Rate: 46.33021045733146
    Zone: Bronx 	 Capture_Rate: 16.469411898376695
    Zone: Bronx 	 Capture_Rate: 34.672869908666286
    Zone: Bronx 	 Capture_Rate: 21.995249858546767


# 5.) Queried Data Selection 
## (alternative to Step 3)

Print out all of the capture rates for recycle bins in The Bronx


```python
# Using make_request() function from step 3

# Get all data from The Bronx
request_url = api_endpoint + "?_zone=Bronx"
json_response, code = make_request(request_url)

# Parse JSON. Notice that we have to grab the first element of the json list and reparse it into JSON.
parsed_json = json.loads(json_response)

print("Zone\t Capture Rates")

for obj in parsed_json:
    print(obj["_zone"], '\t', obj['capture_rate_mgp_total_mgp_max_mgp_'])
```

    Zone	 Capture Rates
    Bronx 	 16.469411898376695
    Bronx 	 34.672869908666286
    Bronx 	 21.995249858546767
    Bronx 	 29.378362098846328
    Bronx 	 39.757652398441685
    Bronx 	 35.21293002170655
    Bronx 	 43.60428817725273
    Bronx 	 59.234563956523814
    Bronx 	 29.10244775033517
    Bronx 	 52.13643352629938
    Bronx 	 44.947038473096264
    Bronx 	 58.78721213791821


If you know the specific values you are looking for, you can query with more finesse. Appending the following to the url to only retreive objects with 'feature' equivilent to 'value':

    ?feature=value
    
e.g:

    ?_zone=Bronx


```python
# Using make_request() function from step 3

# Get all objects from The Bronx with a specific capture rate
request_url = api_endpoint + "?_zone=Bronx&capture_rate_mgp_total_mgp_max_mgp_=52.13643352629938"

# Parse JSON. Notice that we have to grab the first element of the json list and reparse it into JSON.
parsed_json = json.loads(make_request(request_url)[0])

print(parsed_json)
```

    [{'_zone': 'Bronx', 'capture_rate_mgp_total_mgp_max_mgp_': '52.13643352629938', 'capture_rate_paper_total_paper_max_paper_': '43.873033311401834', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '47.011748831050085', 'district': 'BX10', 'diversion_rate_total_total_recycling_total_waste_': '15.41689943656921', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}]



```python
# Using make_request() function from step 3

# Get all data from May 2010
request_url = api_endpoint + "?month_name=May&fiscal_year=2010"
parsed_json = json.loads(make_request(request_url)[0])

print(parsed_json)
```

    [{'_zone': 'Manhattan', 'capture_rate_mgp_total_mgp_max_mgp_': '70.18897504989712', 'capture_rate_paper_total_paper_max_paper_': '54.36418863721333', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '58.17548421760927', 'district': 'MN01', 'diversion_rate_total_total_recycling_total_waste_': '29.27665128471074', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Manhattan', 'capture_rate_mgp_total_mgp_max_mgp_': '78.96740781007655', 'capture_rate_paper_total_paper_max_paper_': '44.3061294956033', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '52.65407008739176', 'district': 'MN02', 'diversion_rate_total_total_recycling_total_waste_': '26.498014918158198', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Manhattan', 'capture_rate_mgp_total_mgp_max_mgp_': '39.4573747627649', 'capture_rate_paper_total_paper_max_paper_': '47.50990064774443', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '43.99317105744572', 'district': 'MN03', 'diversion_rate_total_total_recycling_total_waste_': '13.098489950168535', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Manhattan', 'capture_rate_mgp_total_mgp_max_mgp_': '72.95261708509696', 'capture_rate_paper_total_paper_max_paper_': '37.37981430019573', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '45.94728955709539', 'district': 'MN04', 'diversion_rate_total_total_recycling_total_waste_': '23.12284619426574', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Manhattan', 'capture_rate_mgp_total_mgp_max_mgp_': '66.60389097792556', 'capture_rate_paper_total_paper_max_paper_': '41.13240782129411', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '47.267046776243184', 'district': 'MN05', 'diversion_rate_total_total_recycling_total_waste_': '23.78701035903557', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Manhattan', 'capture_rate_mgp_total_mgp_max_mgp_': '75.99028254954865', 'capture_rate_paper_total_paper_max_paper_': '42.41544252002771', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '50.50172160651501', 'district': 'MN06', 'diversion_rate_total_total_recycling_total_waste_': '25.414851507225517', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Manhattan', 'capture_rate_mgp_total_mgp_max_mgp_': '65.57694753203836', 'capture_rate_paper_total_paper_max_paper_': '43.01477133685949', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '48.448722871767814', 'district': 'MN07', 'diversion_rate_total_total_recycling_total_waste_': '24.381685580830855', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Manhattan', 'capture_rate_mgp_total_mgp_max_mgp_': '64.84051678971925', 'capture_rate_paper_total_paper_max_paper_': '43.50095429530655', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '48.640447372909755', 'district': 'MN08', 'diversion_rate_total_total_recycling_total_waste_': '24.47817040494805', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Manhattan', 'capture_rate_mgp_total_mgp_max_mgp_': '36.0796750024943', 'capture_rate_paper_total_paper_max_paper_': '49.73270669761759', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '43.770103007129954', 'district': 'MN09', 'diversion_rate_total_total_recycling_total_waste_': '13.032073855464882', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Manhattan', 'capture_rate_mgp_total_mgp_max_mgp_': '27.431499457387808', 'capture_rate_paper_total_paper_max_paper_': '33.21156946037611', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '30.687275406081554', 'district': 'MN10', 'diversion_rate_total_total_recycling_total_waste_': '9.136803709369874', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Manhattan', 'capture_rate_mgp_total_mgp_max_mgp_': '23.51529215573911', 'capture_rate_paper_total_paper_max_paper_': '35.79499337952098', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '30.432155771727228', 'district': 'MN11', 'diversion_rate_total_total_recycling_total_waste_': '9.06084460284588', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Manhattan', 'capture_rate_mgp_total_mgp_max_mgp_': '46.33021045733146', 'capture_rate_paper_total_paper_max_paper_': '41.29010346917622', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '43.49123807422963', 'district': 'MN12', 'diversion_rate_total_total_recycling_total_waste_': '12.949044843614862', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Bronx', 'capture_rate_mgp_total_mgp_max_mgp_': '16.469411898376695', 'capture_rate_paper_total_paper_max_paper_': '16.653928911961565', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '16.573345943231484', 'district': 'BX01', 'diversion_rate_total_total_recycling_total_waste_': '4.934534157463125', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Bronx', 'capture_rate_mgp_total_mgp_max_mgp_': '34.672869908666286', 'capture_rate_paper_total_paper_max_paper_': '25.015853213303302', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '29.23330210470515', 'district': 'BX02', 'diversion_rate_total_total_recycling_total_waste_': '8.703898914872951', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Bronx', 'capture_rate_mgp_total_mgp_max_mgp_': '21.995249858546767', 'capture_rate_paper_total_paper_max_paper_': '20.0378044813765', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '20.892667437126633', 'district': 'BX03', 'diversion_rate_total_total_recycling_total_waste_': '6.220565325924603', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Bronx', 'capture_rate_mgp_total_mgp_max_mgp_': '29.378362098846328', 'capture_rate_paper_total_paper_max_paper_': '22.775001484302127', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '25.65884613134602', 'district': 'BX04', 'diversion_rate_total_total_recycling_total_waste_': '7.639643383412663', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Bronx', 'capture_rate_mgp_total_mgp_max_mgp_': '39.757652398441685', 'capture_rate_paper_total_paper_max_paper_': '25.28296246862339', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '31.60440385405769', 'district': 'BX05', 'diversion_rate_total_total_recycling_total_waste_': '9.409868766288431', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Bronx', 'capture_rate_mgp_total_mgp_max_mgp_': '35.21293002170655', 'capture_rate_paper_total_paper_max_paper_': '32.35243265290343', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '33.60167989327626', 'district': 'BX06', 'diversion_rate_total_total_recycling_total_waste_': '10.004536063475422', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Bronx', 'capture_rate_mgp_total_mgp_max_mgp_': '43.60428817725273', 'capture_rate_paper_total_paper_max_paper_': '31.518758465652713', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '36.79679675553842', 'district': 'BX07', 'diversion_rate_total_total_recycling_total_waste_': '10.955847485316482', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Bronx', 'capture_rate_mgp_total_mgp_max_mgp_': '59.234563956523814', 'capture_rate_paper_total_paper_max_paper_': '45.75291494995371', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '50.374829894628725', 'district': 'BX08', 'diversion_rate_total_total_recycling_total_waste_': '16.74396238686484', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Bronx', 'capture_rate_mgp_total_mgp_max_mgp_': '29.10244775033517', 'capture_rate_paper_total_paper_max_paper_': '19.954046070349133', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '23.673691595709894', 'district': 'BX09', 'diversion_rate_total_total_recycling_total_waste_': '7.54720312945949', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Bronx', 'capture_rate_mgp_total_mgp_max_mgp_': '52.13643352629938', 'capture_rate_paper_total_paper_max_paper_': '43.873033311401834', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '47.011748831050085', 'district': 'BX10', 'diversion_rate_total_total_recycling_total_waste_': '15.41689943656921', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Bronx', 'capture_rate_mgp_total_mgp_max_mgp_': '44.947038473096264', 'capture_rate_paper_total_paper_max_paper_': '38.57513879326931', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '40.995399206005786', 'district': 'BX11', 'diversion_rate_total_total_recycling_total_waste_': '13.443914822066052', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Bronx', 'capture_rate_mgp_total_mgp_max_mgp_': '58.78721213791821', 'capture_rate_paper_total_paper_max_paper_': '34.2797367619461', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '43.58849481668533', 'district': 'BX12', 'diversion_rate_total_total_recycling_total_waste_': '14.294287234352312', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Brooklyn North', 'capture_rate_mgp_total_mgp_max_mgp_': '45.564478984843795', 'capture_rate_paper_total_paper_max_paper_': '40.955495780794884', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '42.8294606930384', 'district': 'BKN01', 'diversion_rate_total_total_recycling_total_waste_': '13.65408679371913', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Brooklyn North', 'capture_rate_mgp_total_mgp_max_mgp_': '53.50028330602436', 'capture_rate_paper_total_paper_max_paper_': '35.686874217153125', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '40.95123531121894', 'district': 'BKN02', 'diversion_rate_total_total_recycling_total_waste_': '17.576300079911324', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Brooklyn North', 'capture_rate_mgp_total_mgp_max_mgp_': '33.226543748501705', 'capture_rate_paper_total_paper_max_paper_': '24.181292297167502', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '27.858998006168413', 'district': 'BKN03', 'diversion_rate_total_total_recycling_total_waste_': '8.881484160833725', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Brooklyn North', 'capture_rate_mgp_total_mgp_max_mgp_': '45.22622564226194', 'capture_rate_paper_total_paper_max_paper_': '24.799780705136964', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '33.10496199987881', 'district': 'BKN04', 'diversion_rate_total_total_recycling_total_waste_': '10.553904184989921', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Brooklyn North', 'capture_rate_mgp_total_mgp_max_mgp_': '37.96995353191714', 'capture_rate_paper_total_paper_max_paper_': '23.659090136926658', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '29.477739213921133', 'district': 'BKN05', 'diversion_rate_total_total_recycling_total_waste_': '9.397540926190526', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Brooklyn North', 'capture_rate_mgp_total_mgp_max_mgp_': '46.44529370758909', 'capture_rate_paper_total_paper_max_paper_': '36.76554723413371', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '40.701232058225294', 'district': 'BKN08', 'diversion_rate_total_total_recycling_total_waste_': '12.975604785624641', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Brooklyn North', 'capture_rate_mgp_total_mgp_max_mgp_': '35.06506869864959', 'capture_rate_paper_total_paper_max_paper_': '27.257321859096926', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '30.222965001324003', 'district': 'BKN09', 'diversion_rate_total_total_recycling_total_waste_': '9.911233333923935', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Brooklyn North', 'capture_rate_mgp_total_mgp_max_mgp_': '29.08533254723185', 'capture_rate_paper_total_paper_max_paper_': '22.22892786586633', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '25.016671111650734', 'district': 'BKN16', 'diversion_rate_total_total_recycling_total_waste_': '7.975346715115794', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Brooklyn North', 'capture_rate_mgp_total_mgp_max_mgp_': '51.282617855671994', 'capture_rate_paper_total_paper_max_paper_': '29.983957726596234', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '38.073900529357196', 'district': 'BKN17', 'diversion_rate_total_total_recycling_total_waste_': '12.485846840723196', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Brooklyn South', 'capture_rate_mgp_total_mgp_max_mgp_': '76.52499061442046', 'capture_rate_paper_total_paper_max_paper_': '48.48143844539721', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '56.76909322509025', 'district': 'BKS06', 'diversion_rate_total_total_recycling_total_waste_': '24.36533623969323', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Brooklyn South', 'capture_rate_mgp_total_mgp_max_mgp_': '59.37120894107333', 'capture_rate_paper_total_paper_max_paper_': '47.79892518588103', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '52.19446523908006', 'district': 'BKS07', 'diversion_rate_total_total_recycling_total_waste_': '17.116504740724228', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Brooklyn South', 'capture_rate_mgp_total_mgp_max_mgp_': '61.92635261586691', 'capture_rate_paper_total_paper_max_paper_': '61.48980835376911', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '61.655622451456104', 'district': 'BKS10', 'diversion_rate_total_total_recycling_total_waste_': '20.219169774968485', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Brooklyn South', 'capture_rate_mgp_total_mgp_max_mgp_': '52.91748987503592', 'capture_rate_paper_total_paper_max_paper_': '53.91452411975474', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '53.535817198132094', 'district': 'BKS11', 'diversion_rate_total_total_recycling_total_waste_': '17.55638389382842', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Brooklyn South', 'capture_rate_mgp_total_mgp_max_mgp_': '41.03120188064101', 'capture_rate_paper_total_paper_max_paper_': '48.10278451746811', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '45.22755214000947', 'district': 'BKS12', 'diversion_rate_total_total_recycling_total_waste_': '14.41860141114321', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Brooklyn South', 'capture_rate_mgp_total_mgp_max_mgp_': '38.853636257665094', 'capture_rate_paper_total_paper_max_paper_': '44.37807294371361', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '41.96542003938732', 'district': 'BKS13', 'diversion_rate_total_total_recycling_total_waste_': '12.494749058274216', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Brooklyn South', 'capture_rate_mgp_total_mgp_max_mgp_': '45.134475783548375', 'capture_rate_paper_total_paper_max_paper_': '37.27957745666489', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '39.97247295841195', 'district': 'BKS14', 'diversion_rate_total_total_recycling_total_waste_': '13.286349256674827', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Brooklyn South', 'capture_rate_mgp_total_mgp_max_mgp_': '52.51456794861542', 'capture_rate_paper_total_paper_max_paper_': '55.319132864398746', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '54.25386539603139', 'district': 'BKS15', 'diversion_rate_total_total_recycling_total_waste_': '17.79185858117534', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Brooklyn South', 'capture_rate_mgp_total_mgp_max_mgp_': '59.34628033032124', 'capture_rate_paper_total_paper_max_paper_': '43.78507824885981', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '49.31810462506259', 'district': 'BKS18', 'diversion_rate_total_total_recycling_total_waste_': '14.443406036847497', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Queens West', 'capture_rate_mgp_total_mgp_max_mgp_': '57.544145633201495', 'capture_rate_paper_total_paper_max_paper_': '54.79961348889329', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '55.842078504684665', 'district': 'QW01', 'diversion_rate_total_total_recycling_total_waste_': '18.31269267879514', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Queens West', 'capture_rate_mgp_total_mgp_max_mgp_': '59.681346020409066', 'capture_rate_paper_total_paper_max_paper_': '54.976129938734296', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '56.76332822936365', 'district': 'QW02', 'diversion_rate_total_total_recycling_total_waste_': '18.61480469790731', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Queens West', 'capture_rate_mgp_total_mgp_max_mgp_': '51.30230288807635', 'capture_rate_paper_total_paper_max_paper_': '33.533666946403415', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '40.2827886085206', 'district': 'QW03', 'diversion_rate_total_total_recycling_total_waste_': '13.210223325960586', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Queens West', 'capture_rate_mgp_total_mgp_max_mgp_': '41.39233719979363', 'capture_rate_paper_total_paper_max_paper_': '34.86907822272402', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '37.346829954160285', 'district': 'QW04', 'diversion_rate_total_total_recycling_total_waste_': '12.247413380581515', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Queens West', 'capture_rate_mgp_total_mgp_max_mgp_': '64.40445011177978', 'capture_rate_paper_total_paper_max_paper_': '55.63134245770429', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '58.96366189441127', 'district': 'QW05', 'diversion_rate_total_total_recycling_total_waste_': '19.336375872867155', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Queens West', 'capture_rate_mgp_total_mgp_max_mgp_': '59.67812144280414', 'capture_rate_paper_total_paper_max_paper_': '31.02685429040165', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '37.92732327765892', 'district': 'QW06', 'diversion_rate_total_total_recycling_total_waste_': '19.086820379681665', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Queens West', 'capture_rate_mgp_total_mgp_max_mgp_': '56.38234682385516', 'capture_rate_paper_total_paper_max_paper_': '42.33504394277595', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '47.67067896170619', 'district': 'QW09', 'diversion_rate_total_total_recycling_total_waste_': '15.632987112791568', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Queens East', 'capture_rate_mgp_total_mgp_max_mgp_': '51.07112078120035', 'capture_rate_paper_total_paper_max_paper_': '53.01469503215925', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '52.27646058793184', 'district': 'QE07', 'diversion_rate_total_total_recycling_total_waste_': '17.14339406262667', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Queens East', 'capture_rate_mgp_total_mgp_max_mgp_': '43.76543343435467', 'capture_rate_paper_total_paper_max_paper_': '32.43299688688826', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '35.782049152168725', 'district': 'QE08', 'diversion_rate_total_total_recycling_total_waste_': '15.357681608211635', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Queens East', 'capture_rate_mgp_total_mgp_max_mgp_': '70.58154323757502', 'capture_rate_paper_total_paper_max_paper_': '45.794356095774155', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '54.60782433103648', 'district': 'QE10', 'diversion_rate_total_total_recycling_total_waste_': '15.992564710225812', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Queens East', 'capture_rate_mgp_total_mgp_max_mgp_': '67.17015956027149', 'capture_rate_paper_total_paper_max_paper_': '65.5725934172423', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '66.14063279882964', 'district': 'QE11', 'diversion_rate_total_total_recycling_total_waste_': '19.370087766147947', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Queens East', 'capture_rate_mgp_total_mgp_max_mgp_': '48.6911499925129', 'capture_rate_paper_total_paper_max_paper_': '39.083195590399214', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '43.49410874617291', 'district': 'QE12', 'diversion_rate_total_total_recycling_total_waste_': '11.95382734141861', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Queens East', 'capture_rate_mgp_total_mgp_max_mgp_': '67.03055165613388', 'capture_rate_paper_total_paper_max_paper_': '41.85702828843178', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '50.80786435150099', 'district': 'QE13', 'diversion_rate_total_total_recycling_total_waste_': '14.8797002697641', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Queens East', 'capture_rate_mgp_total_mgp_max_mgp_': '34.90543395388806', 'capture_rate_paper_total_paper_max_paper_': '32.0048158006721', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '33.10656749819475', 'district': 'QE14', 'diversion_rate_total_total_recycling_total_waste_': '10.856873749664736', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Staten Island', 'capture_rate_mgp_total_mgp_max_mgp_': '60.78740386292506', 'capture_rate_paper_total_paper_max_paper_': '46.9541455717905', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '51.87277477491984', 'district': 'SI01', 'diversion_rate_total_total_recycling_total_waste_': '15.191572223385233', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Staten Island', 'capture_rate_mgp_total_mgp_max_mgp_': '65.53969008221074', 'capture_rate_paper_total_paper_max_paper_': '54.17105632593259', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '58.21335010925248', 'district': 'SI02', 'diversion_rate_total_total_recycling_total_waste_': '17.04848673291907', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}, {'_zone': 'Staten Island', 'capture_rate_mgp_total_mgp_max_mgp_': '67.89551007280613', 'capture_rate_paper_total_paper_max_paper_': '57.73705128736698', 'capture_rate_total_total_recycling_leaves_recycling_max_paper_max_mgp_x100': '61.34904861939605', 'district': 'SI03', 'diversion_rate_total_total_recycling_total_waste_': '17.96681413287608', 'fiscal_month_number': '11', 'fiscal_year': '2010', 'month_name': 'May', 'report_version': 'Preliminary'}]

