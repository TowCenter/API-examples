# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:24:16 2018

@author: emrig

This script compiles and executes API queries to the US Census Bureau. 
See supporting doc: https://github.com/TowCenter/API-examples/blob/master/Census-API/Census_API_Guide.md
"""

#from census_api_key import API_key 
import urllib
import json

base_url = 'https://api.census.gov/data/2014/pep/natstprc'
    
#complete URL string
req_url = base_url + '?' + 'get=STNAME,DENSITY&DATE=7&for=state:*'

#urllib function to request over http:
req = urllib.request.Request(req_url)

with urllib.request.urlopen(req) as response:
   raw = response.read()

#print results in json format
results = json.loads(raw)

for result in results: print(result)
