## NASA API Demo

## Once you recieve you API credentials, I recommend storing it as a variable in another file.
## In this example, I created another python file called "NASA_API_Credentials.py" and stored
## it in the same folder as NASA_API_Demo.py. Inside that file, I created a variable api_key
## and set it equal to my personal NASA api key like so:
## api_key = "your_api_key____This_should_be_a_string_of_letters_and_numbers" 

##This line allows you to call the api_key variable you made in your other file, in this one
from NASA_API_Credentials import api_key 
import requests #A basic python package for making http requests



## This python demo assumes you have read the associated API tutorial. If you haven't already,
## refer to NASA_API_Profile.md to learn about the functionality of this API. 
## 
## We will now use python to make run the three query examples from that tutorial 


# base url. Every http request to the Rover API will start with this string
base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/"


### Query 1

### We want to construct a URL that will return us the 26th through 50th picture taken
### by Opportunity's panoramic camera on June 3, 2015

rover = "opportunity"
earth_date = "2015-6-3" 
camera = "pancam" 
page_number = "2"

# Add these variables into one url that we can use
request_url = "{}{}/photos?earth_date={}&camera={}&page={}&api_key={}".format(base_url,rover,earth_date,camera,page_number,api_key)


query1 = requests.get(request_url).json() #requests.get() is a function that returns information stored on a html page. json() converts the json object into a readable format for this program 

#Printing this query will return the same output had you typed this url directly into your browser. 
print(query1)

# If you wanted to do something with this information, like display it on a website, you 
# can use Python to extract pieces of information from this string. However, working with
# JSON objects is a matter for a different tutorial. 


### Query 2

### We want to construct a URL that will return us all the photos Spirit took on its first day
### on Mars

rover = "spirit"
mars_sol = "1" 

request_url = "{}{}/photos?sol={}&api_key={}".format(base_url,rover,mars_sol,api_key)

query2 = requests.get(request_url).json()

print(query2)

### Query 3

### We want to construct a URL that will get the 101st to 125th photo Spirit took on its
### first day on Mars

rover = "spirit"
mars_sol = "1"
page_number = "5"

request_url = "{}{}/photos?sol={}&page={}&api_key={}".format(base_url,rover,mars_sol,page_number,api_key)

query3 = requests.get(request_url).json()

print(query3)