# NASA API Profile

NASA's APIs give developers access to a wide variety of agency data. The information accessible through these APIs range from an archive of exoplanet data to outer space weather forecasts. For the purpose of this demo, I have focused on the "Mars Rover Images" API, which makes available image data from NASA's Curiosity, Opportunity, and Spirit rovers. 

For access to all of NASA's APIs, visit https://api.nasa.gov/index.html. 

The Mars Rover Photo API was built and is maintained by Chris Cerami, an independent developer. In-depth inquiries should be directed to Cerami at chrisccerami@gmail.com or via Twitter at @chrisccerami. NASA encourages contributions to its growing list of APIs.   
Check out NASA_API_Demo.py in this Github repo for a companion tutorial on how to make requests to this API using python.

## Setup

### Step 1: Get your unique API key

Many API's require developers to apply for a unique key. This key is a password of sorts for the API and allows NASA to track data usage. To get a NASA API key, navigate to https://api.nasa.gov/index.html if you haven't already. Scroll down to the "Get Your API Key" header and fill out the form. You should immediately receive a unique key consisting of a string of letters and numbers. **Save this string**.

### Step 2: Navigate to Mars photos API page

Navigate to the Mars Rover Photos API using this URL: https://api.nasa.gov/api.html#MarsPhotos. You *can* get to this page from the NASA API homepage where you got your key, but I recommend using the link above as navigation on the site is a little wonky. Here you will find a brief tutorial on the purpose of the API and how to use it. Cerami also wrote his own tutorial that you can find on his personal Github page here: https://github.com/chrisccerami/mars-photo-api

#### A quick aside about APIs

Many APIs, like the Mars rover photos API, return information using a URL. In these cases, you can ask for certain bits of information in an API's database by adding variables to the URL. Then, you can run the URL through your browser and your browser will return a package of information. In the case of the Mars rover photos API, it returns its information as a JSON object. If you don't know what a JSON object is, [here](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON) is a not-very-brief description of them. Just knowing their basic structure is more than enough to understand this API. 

We will cover the different variables at your disposal in a later section. 

### Step 3: Try out this example query

https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY

This query returns information on all the photos taken by the Curiosity rover on its 1000th Martian day. You can swap out "DEMO_KEY" for your own API key and the url will return the same information. Remove "DEMO_KEY" without replacing with your own key and you can 
see how an API key acts as a kind of password. Note the variables at play such as "sol=1000". Change "1000" to "900" and the url still provides information. In this case, it will be all the photos taken by Curiosity on its 900th Martian Day. 
    
This is the basis for how all these API requests work. Change variables and the format of the url and you will receive different bits of information.

### Step 3: Did something break?

Current documentation states that, in addition to photo information, you should also be able to access manifests and latest photos for each rover. As of Feb. 2, 2019, I don't think these two features are functional. This issue may be fixed at some point.

## Variables

When building a url for this API, there are three categories of variables:
	
### 1. Rovers: Curiosity, Opportunity, Spirit  

When searching for photos, you must limit your search to one of the three available rovers.

ex: *.../rovers/curiosity/photos?...*

ex: *.../rovers/opportunity/photos?...*

ex: *.../rovers/spirit/photos?...*

### 2. Filter: Earth day, Martian sol, Camera type  

After selecting a rover, you can filter the photo results based on these three variables. You **must** include at least one of these filters. Earth day represents the day on earth the photo was taken. Earth day and Martian sol can be used in tandem with Camera type, but Earth day and Martian sol cannot be used together. Earth day should be added with a YYYY-MM-DD format and Martian sol represents a number 0 to the total number of days a rover has been on Mars. Camera allows you to select photos from specific cameras on each rover. Leaving the camera variable blank will return photos from every camera on the rover. 

Cerami assembled a table to list which cameras are mounted on each rover. Use this table as a reference for effecively using the API. When you are ready to send a query, use the abbreviation of a camera to select it. i.e. *.../photos?camera=mardi&api_key=API_key*

  Abbreviation | Camera                         | Curiosity | Opportunity | Spirit
  ------------ | ------------------------------ | --------  | ----------- | ------ |
   FHAZ|Front Hazard Avoidance Camera|✔|✔|✔|
   RHAZ|Rear Hazard Avoidance Camera|✔|✔|✔|
   MAST|Mast Camera| ✔|
   CHEMCAM|Chemistry and Camera Complex  | ✔| 
   MAHLI|Mars Hand Lens Imager|✔| 
   MARDI|Mars Descent Imager|✔|
   NAVCAM|Navigation Camera|✔|✔|✔|
   PANCAM|Panoramic Camera|-|✔|✔|
   MINITES|Miniature Thermal Emission Spectrometer (Mini-TES)|-|✔|✔|

#### How to learn a rover's functioning lifespan:
When selecting Earth date or Martian Sol, your query will **only** return photos if your dates are within the rover's functioning lifespan. If the rover manifest feature of this API was functional, this would be easy information to find. However, you can still find a rover's operating range without it. Run any simple photo query for any rover in your browser. https://api.nasa.gov/mars-photos/api/v1/rovers/Opportunity/photos?sol=3&page=1&api_key=DEMO_KEY works well. CTRL-F "landing_date" in the resulting json text and you will see the first Earth date a rover was on Mars. Do the same for "max_date" and "max_sol" and you will see the maximum Earth date and maximum sol you can input.

ex: *.../photos?sol=1000&api_key=API_key* 

ex: *.../photos?earth_date=2016-5-25&camera=fhaz&api_key=API_key*   

### 3. Page: 1, 2, 3, etc.

If the API request returns too many results, you can limit them by setting a page number. Pages limit the results to 25 photos. **Be advised**, if you set a page number and return an empty set, it could be because there were only 25 photo entries on that day in the first place. 

ex: *.../photos?sol=1000&page=2&api_key=API_key*
	  
## Example API requests

### Query 1
**url:** https://api.nasa.gov/mars-photos/api/v1/rovers/Opportunity/photos?earth_date=2015-6-3&camera=pancam&page=2&api_key=API_key

**Rover:** Opportunity  
  *Selects the Opportunity rover*

**Filters:** earth_date=2015-6-3, camera=pancam  
  *Selects only photos taken with the panoramic camera on June 3, 2015* 

**Page:** 2  
  *Only returns the 26th through 50th photo that day* 
  
**Returns:**  

{"photos":[{"id":106898,"sol":4037,"camera":{"id":17,"name":"PANCAM","rover_id":6,"full_name":"Panoramic Camera"},"img_src":"http://mars.nasa.gov/mer/gallery/all/1/p/4037/1P486570059EFFCNJDP2407R2M1-BR.JPG","earth_date":"2015-06-03","rover":{"id":6,"name":"Opportunity","landing_date":"2004-01-25","launch_date":"2003-07-07","status":"active","max_sol":5111,"max_date":"2018-06-11","total_photos":198439,"cameras":[{"name":"FHAZ","full_name":"Front Hazard Avoidance Camera"},{"name":"NAVCAM","full_name":"Navigation Camera"},{"name":"PANCAM","full_name":"Panoramic Camera"},{"name":"MINITES","full_name":"Miniature Thermal Emission Spectrometer (Mini-TES)"},{"name":"ENTRY","full_name":"Entry, Descent, and Landing Camera"},{"name":"RHAZ","full_name":"Rear Hazard Avoidance Camera"}]}}]}

**Explaination:** 

Each photo has a unique id. As it happens, Opportunity only took 26 photos on it's panoramic camera on June 3, 2015. Therefore, only one photo is returned on the proverbial second page. Each photo contains a small package of photo-specific data and data about the rover. That includes how many days the rover had been on Mars before the photo was taken (4037). You also receive a url of where you can find the photo online. Feel free to view the photo, but it is not that exciting (other than the fact it was taken on a different planet). Finally, each package of photo data also includes information about the rover that took it. For example, the "launch_date" of the rover was July 7, 2003. The "max_date," or last time photos were pinged back to Earth, is June 11, 2018. A day later, a dust storm forced Opportunity into hibernation. NASA has not been able to reestablish contact, since. Nasa officially retired Opportunity on Feburary 13, 2019 after 5,352 sols, over 14 Earth years on the Martian surface. 

### Query 2
**url:** https://api.nasa.gov/mars-photos/api/v1/rovers/spirit/photos?sol=1&api_key=API_key

**Rover:** Spirit  
*Selects the Spirit rover*

**Filters:** sol=1  
*Selects only photos taken by the Spirit rover on its first Martian day*

**Page:** N/A  
*No page filter returns all the photos taken on Martian day 1*

**Returns:** 

{"photos":[{"id":287319,"sol":1,"camera":{"id":27,"name":"FHAZ","rover_id":7,"full_name":"Front Hazard Avoidance Camera"},"img_src":"http://mars.nasa.gov/mer/gallery/all/2/f/001/2F126468064EDN0000P1001L0M1-BR.JPG","earth_date":"2004-01-05","rover":{"id":7,"name":"Spirit","landing_date":"2004-01-04","launch_date":"2003-06-10","status":"complete","max_sol":2208,"max_date":"2010-03-21","total_photos":124550,"cameras":[{"name":"FHAZ","full_name":"Front Hazard Avoidance Camera"},{"name":"NAVCAM","full_name":"Navigation Camera"},{"name":"PANCAM","full_name":"Panoramic Camera"},{"name":"MINITES","full_name":"Miniature Thermal Emission Spectrometer (Mini-TES)"},{"name":"ENTRY","full_name":"Entry, Descent, and Landing Camera"},{"name":"RHAZ","full_name":"Rear Hazard Avoidance Camera"}]}},{"id":287320,"sol":1,"camera":{"id":27,"name":"FHAZ","rover_id":7,"full_name":"Front Hazard Avoidance Camera"},"img_src":"http://mars.nasa.gov/mer/gallery/all/2/f/001/2F126468064EDN0000P1001R0M1-BR.JPG","earth_date":"2004-01-05","rover":{"id":7,"name":"Spirit","landing_date":"2004-01-04","launch_date":"2003-06-10","status":"complete","max_sol":2208,"max_date":"2010-03-21","total_photos":124550,"cameras":[{"name":"FHAZ","full_name":"Front Hazard Avoidance Camera"},{"name":"NAVCAM","full_name":"Navigation Camera"},{"name":"PANCAM","full_name":"Panoramic Camera"},{"name":"MINITES","full_name":"Miniature Thermal Emission Spectrometer (Mini-TES)"},{"name":"ENTRY","full_name":"Entry, Descent, and Landing Camera"},{"name":"RHAZ","full_name":"Rear Hazard Avoidance Camera"}]}},{"id":290673,"sol":1,"camera":{"id":28,"name":"RHAZ","rover_id":7,"full_name":"Rear Hazard Avoidance Camera"},"img_src":"http://mars.nasa.gov/mer/gallery/all/2/r/001/2R126468012EDN0000P1002L0M1-BR.JPG","earth_date":"2004-01-05","rover":{"id":7,"name":"Spirit","landing_date":"2004-01-04","launch_date":"2003-06-10","status":"complete","max_sol":2208,"max_date":"2010-03-21","total_photos":124550,"cameras":[{"name":"FHAZ","full_name":"Front Hazard Avoidance Camera"},{"name":"NAVCAM","full_name":"Navigation Camera"},{"name":"PANCAM","full_name":"Panoramic Camera"},{"name":"MINITES","full_name":"Miniature Thermal Emission Spectrometer (Mini-TES)"},{"name":"ENTRY","full_name":"Entry, Descent, and Landing Camera"},{"name":"RHAZ","full_name":"Rear Hazard Avoidance Camera"}]}},{"id":290674,"sol":1,"camera":{"id":28,"name":"RHAZ","rover_id":7,"full_name":"Rear Hazard Avoidance Camera"},"img_src":"http://mars.nasa.gov/mer/gallery/all/2/r/001/2R126468012EDN0000P1002R0M1-BR.JPG","earth_date":"2004-01-05","rover":{"id":7,"name":"Spirit","landing_date":"2004-01-04","launch_date":"2003-06-10","status":"complete","max_sol":2208,"max_date":"2010-03-21","total_photos":124550,"cameras":[{"name":"FHAZ","full_name":"Front Hazard Avoidance Camera"},{"name":"NAVCAM","full_name":"Navigation Camera"},{"name":"PANCAM","full_name":"Panoramic Camera"},{"name":"MINITES","full_name":"Miniature Thermal Emission Spectrometer (Mini-TES)"},{"name":"ENTRY","full_name":"Entry, Descent, and Landing Camera"},{"name":"RHAZ","full_name":"Rear Hazard Avoidance Camera"}]}},{"id":318416,"sol":1,"camera":{"id":29,"name":"NAVCAM","rover_id":7,"full_name":"Navigation Camera"},"img_src":"http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126467960EDN0000P1500L0M1-BR.JPG","earth_date":"2004-01-05","rover":{"id":7,"name":"Spirit","landing_date":"2004-01-04","launch_date":"2003-06-10","status":"complete","max_sol":2208,"max_date":"2010-03-21","total_photos":124550,"cameras":[{"name":"FHAZ","full_name":"Front Hazard Avoidance Camera"},{"name":"NAVCAM","full_name":"Navigation Camera"},{"name":"PANCAM","full_name":"Panoramic Camera"},{"name":"MINITES","full_name":"Miniature Thermal Emission Spectrometer (Mini-TES)"},{"name":"ENTRY","full_name":"Entry, Descent, and Landing Camera"},{"name":"RHAZ","full_name":"Rear Hazard Avoidance Camera"}]}},{"id":318417,"sol":1,"camera":{"id":29,"name":"NAVCAM","rover_id":7,"full_name":"Navigation Camera"},"img_src":"http://mars.nasa.gov/mer/gallery/all/2/n/001/2N126467960EDN0000P1500R0M1-BR.JPG","earth_date":"2004-01-05","rover":{"id":7,"name":"Spirit","landing_date":"2004-01-04","launch_date":"2003-06-10","status":"complete","max_sol":2208,"max_date":"2010-03-21","total_photos":124550,"cameras":[{"name":"FHAZ","full_name":"Front Hazard Avoidance Camera"},{"name":"NAVCAM","full_name":"Navigation Camera"},{"name":"PANCAM","full_name":"Panoramic Camera"},{"name":"MINITES","full_name":"Miniature Thermal Emission Spectrometer (Mini-TES)"},{"name":"ENTRY","full_name":"Entry, Descent, and Landing Camera"},{"name":"RHAZ","full_name":"Rear Hazard Avoidance Camera"}]}}

**Explaination:**


Above is a small snippet of the json object returned by this API request. The data format is the same as the previous query. This is an interesting query to run if you want to see the first photos the Spirit rover took on Mars.

### Query 3
**url:** https://api.nasa.gov/mars-photos/api/v1/rovers/spirit/photos?sol=1&page=5&api_key=API_key

**Rover:** Spirit  
*Selects the spirit rover*

**Filters:** sol=1  
*Selects only photos taken by the Spirit rover on its first Martian day*
**Page:** 5  
*Selects only the 101-125th photos taken that sol*

**Returns:** 

{"photos":[]}

**Explaination:** 

Don't be shocked. What this result tells you is that the Spirit rover did not take more than
100 photos on its first Martian day. With no photos, the API returns an Empty set. 

## Limitations

NASA's APIs and the data they provide are completely free for both private and comercial use.

However, http requests from a single API key are capped at 1,000  per hour. Once that number is exceeded, requests using that API key are temporarily blocked. As long as you use the same API key, this limit extends across APIs. You cannot make 500 requests from the [Techport API](https://api.nasa.gov/api.html#genelab) and 600 requests from the [GeneLab Search API](https://api.nasa.gov/api.html#genelab) in the same hour using your same API key. 
  
The http request counter resets on a rolling basis. If you make 100 requests at 10:15 a.m. and 900 requests at 10:30 a.m., your API key will be prevented from making any more 
requests until 11:15. Now, you can make 100 more requests. If you require more than 1000 
requests per hour, you can contact Jason Duley at jason.duley@nasa.gov to request a 
higher rate limit for your API key. 

## Process Log

1. My starting point was https://api.nasa.gov/index.html
2. I worked my way down this page, reading up on the API and signing up for a API Key. I stored that API Key in a separate file from NASA_API_Demo.py
3. Near the bottom of the page, underneath the "Authentication," are the next set of directions for using your API Key. In short, they tell you to click on a hyperlink and go to this page: https://api.nasa.gov/api.html#authentication Not the smoothest UI experience, but it's no problem. 
4. Once on this page, I read up on the API key request limit. I then tested out queries for the different API's. Luckily there is not much documentation other than showing the url requests. There is plenty of room for expanding on how to effectively use these requests in python.  
5. I settled on the Mars Rover API. Under that API's heading, I found a link to Chris Cerami's GitHub page https://github.com/chrisccerami/mars-photo-api, which has more info on how to use his API. I primarily used the API documentation on Cerami's GitHub page to guide my exploration. 
6. I played around with several different variable combinations.  
7. I came to an issue where some of the queries in the initial documentation do not work anymore. I left a issue post on Cerami's GitHub repository. https://github.com/chrisccerami/mars-photo-api/issues/82
8. I started writing up the documentation. As a matter of small interest, while writing up query 1, I noticed that Opportunity last ping date was June 11, 2018. That is the a day before dust storm forced the rover into hibernation. NASA has not been able to reestablish contact.
