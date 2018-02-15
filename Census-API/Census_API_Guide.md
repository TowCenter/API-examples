
Erin Riglin - er2865 - Investigative Techniques - Assignment 2.2

# Census Bureau API Guide

The United States Census Bureau is a government agency responsible for collecting population data within the United States every 10 years. They have made their extensive data sets available to the general public by releasing easy-to-use APIs through which users can query economic information such as population, race, and age statistics for any given geographical area.


## Data Sets

Various data sets are available for querying. They differ by survey methodology and frequency, and therefore contain different types of data such as housing, business, or migration information. The URL endpoint you will use is dependent on the data set you decide to query. 

A list of data sets and their base URL mappings can be found here:

[https://api.census.gov/data.html](https://api.census.gov/data.html)


## API Attributes

For the purpose of this walkthrough, we will perform our queries using Python 3.6. From a Python editor, import the following libraries:


```python
import urllib   #library for URL requests
import json     #library for JSON response formatting
```

### Base URL

We will use the *Vintage 2014 Population Estimates: US, State, and PR Total Population and Components of Change* dataset which is a collection of population and demographics statistics from 2010-2014. The base URL for this dataset is:


```python
base_url = 'https://api.census.gov/data/2014/pep/natstprc'
```

### Variables

Each data set has a set of variables representing data types that can be fetched or used to filter your query. Construction of your query depends on the type of information you would like to get.

The variables for the *Vintage 2014 Population Estimates: US, State, and PR Total Population and Components of Change* data set can be found here:   
  
[https://api.census.gov/data/2014/pep/natstprc/variables.html](https://api.census.gov/data/2014/pep/natstprc/variables.html)


Predicate variables are used to limit the scope of the search and are preceded by an ampersand (&) within the search URL followed by a parameter. 

### Complete URL

A search URL should contain the (1) base URL, (2) at least one variable to retrieve, and at least one (3) predicate variable for filtering:

Example of a query that displays all state names and their population:  
  
https://api.census.gov/data/2014/pep/natstprc?get=STNAME&DATE=7&for=state:*

__Base URL:__ https://api.census.gov/data/2014/pep/natstprc  
__Variables to Retrieve:__ State Name (STNAME)  
__Predicate Variables:__ Complete Data Range (DATE=7) and all states by State ID (for=state:*)

## Python

The below Python example can be found [here.](https://github.com/TowCenter/API-examples/blob/master/Census-API/census_api.py)

To execute the above query in Python, we write:


```python
#complete URL string
req_url = base_url + '?' + 'get=STNAME&DATE=7&for=state:*'

#urllib function to request over http:
req = urllib.request.Request(req_url)

with urllib.request.urlopen(req) as response:
   raw = response.read()

#print results in json format
results = json.loads(raw)
for result in results: print(result)
```

    ['STNAME', 'DATE', 'state']
    ['Alabama', '7', '01']
    ['Alaska', '7', '02']
    ['Arizona', '7', '04']
    ['Arkansas', '7', '05']
    ['California', '7', '06']
    ['Colorado', '7', '08']
    ['Connecticut', '7', '09']
    ['Delaware', '7', '10']
    ['District of Columbia', '7', '11']
    ['Florida', '7', '12']
    ['Georgia', '7', '13']
    ['Hawaii', '7', '15']
    ['Idaho', '7', '16']
    ['Illinois', '7', '17']
    ['Indiana', '7', '18']
    ['Iowa', '7', '19']
    ['Kansas', '7', '20']
    ['Kentucky', '7', '21']
    ['Louisiana', '7', '22']
    ['Maine', '7', '23']
    ['Maryland', '7', '24']
    ['Massachusetts', '7', '25']
    ['Michigan', '7', '26']
    ['Minnesota', '7', '27']
    ['Mississippi', '7', '28']
    ['Missouri', '7', '29']
    ['Montana', '7', '30']
    ['Nebraska', '7', '31']
    ['Nevada', '7', '32']
    ['New Hampshire', '7', '33']
    ['New Jersey', '7', '34']
    ['New Mexico', '7', '35']
    ['New York', '7', '36']
    ['North Carolina', '7', '37']
    ['North Dakota', '7', '38']
    ['Ohio', '7', '39']
    ['Oklahoma', '7', '40']
    ['Oregon', '7', '41']
    ['Pennsylvania', '7', '42']
    ['Rhode Island', '7', '44']
    ['South Carolina', '7', '45']
    ['South Dakota', '7', '46']
    ['Tennessee', '7', '47']
    ['Texas', '7', '48']
    ['Utah', '7', '49']
    ['Vermont', '7', '50']
    ['Virginia', '7', '51']
    ['Washington', '7', '53']
    ['West Virginia', '7', '54']
    ['Wisconsin', '7', '55']
    ['Wyoming', '7', '56']
    ['Puerto Rico Commonwealth', '7', '72']
    

The result is a  list of states and territories along with the corresponding State ID (state).

Knowing each State ID now allows us to refine our queries to the state level. To obtain the population of New York in 2014 we write:  


```python
#complete URL string
req_url = base_url + '?' + 'get=STNAME,POP&DATE=7&for=state:36'

#urllib function to request over http:
req = urllib.request.Request(req_url)

with urllib.request.urlopen(req) as response:
   raw = response.read()

#print results in json format
results = json.loads(raw)
for result in results: print(result)
```

    ['STNAME', 'POP', 'DATE', 'state']
    ['New York', '19746227', '7', '36']
    

And finally a query for the population (POP), Density (DENSITY), Total Births (BIRTHS) in the entire United States in 2014:


```python
#complete URL string
req_url = base_url + '?' + 'get=STNAME,POP,DENSITY,BIRTHS&DATE=7&for=us:*'

#urllib function to request over http:
req = urllib.request.Request(req_url)

with urllib.request.urlopen(req) as response:
   raw = response.read()

#print results in json format
results = json.loads(raw)
for result in results: print(result)
```

    ['STNAME', 'POP', 'DENSITY', 'BIRTHS', 'DATE', 'us']
    ['United States', '318857056', '90.278357722', '3957577', '7', '00']
    

## API Key Requirement

The Census Bureau API documentation mentions a developer key requirement to utilize their APIs, but testing across various data sets and query types proved a key to be unnecessary. If you receive an error code response that states an API key requirement, you can request one here:

https://api.census.gov/data/key_signup.html

Once you receive your key, append this string to the end of each web request:


```python
#add developer key
req_url += '&key=<your key here>'
```

## Query Limits

Across all data sets an individual can submit a maximum of 500 queries from a single IP address per day. Each query can take a maximum of 50 variables.

# Additional Links

Census Bureau Developer Page: https://www.census.gov/developers/  
Census Bureau API Guide: https://www.census.gov/content/dam/Census/data/developers/api-user-guide/api-guide.pdf  
Census Bureau Data Sets: https://api.census.gov/data.html  

