# API: NYC 311 API


I have chosen the API of NYC 311 service requests, which contains all service requests data from October, 2010 to present. The source domain is data.cityofnewyork.us with the dataset identifier fhrw-4uyv. The endpoint version is 2.1. We are allowed to make a limited number of requests of this API without an app token. But if we need more requests, we will have to sign up for an app token for each request. This API will help me to come up with a lot of stories, including complaints about noises, transportation, street, public services, etc, which will be very useful.

* My queries are as following: 

1. URL:

`<https://data.cityofnewyork.us/resource/fhrw-4uyv.json? complaint_type=Noise&borough=MANHATTAN&community_board=10 MANHATTAN&$select=resolution_description&$where=created_date between '2010-10-10T00:00:00.000' and '2012-01-01T00:00:00.000'>` 


I searched all the complaints about noise in Community Board 10 of Manhattan Borough, which created between 2010-10-10 and 2012-01-01. I only selected the resolution description column to see all the resolutions. So the response only includes the resolution description under above conditions. The resolution description describes the last action taken on the SR by the responding agency, which may also describe next or future steps. From the resolution description, we could get statistics about like how many noise complaints were not observed by the Department of Environmental Protection, how many were duplicated with previous complaints( which means that the noise was complained several times),etc. For example, we could classify the resolutions to report about the actions of the responding agency.

2. URL:

`<https://data.cityofnewyork.us/resource/fhrw-4uyv.json? borough=MANHATTAN&agency=DOE&status=Closed&$where=school_number between '001' and ‘010'>`

I searched all the complaints about schools in Manhattan, with school number between 001 to 010, agency of DOE(Department of Education) and status is closed. The responses contain all the information of these service requests forms, including the agency information, community board, complaint types, created date and closed date, cross street about the complaint, incident street and zip, latitude and longitude, location point, the information of the school(school number, school region, and so on). We could analyze from these information and find out which school or borough has the most complaints or which type of complaints happened mostly in 311 forms.

3. URL:

`<https://data.cityofnewyork.us/resource/fhrw-4uyv.json  taxi_company_borough=MANHATTAN&agency=DOT&$where=intersection_street_1='BROAD WAY' or intersection_street_2=‘Broadway’&$select=unique_key>`

In this query, I searched the unique key of all the complaints about taxi which the company is in Manhattan. The complaints were responded by Department of Transportation, and it happened on the street of Broadway. The responses contain only the unique key of complaints under conditions above. The unique key can uniquely identify a Service Request form in the data set. By using these unique keys, we could calculate how many complaints have been made about taxi under above conditions. And we could easily obtain one specific complaint by selecting the unique key we have gotten.

# Log:
1. I found the NYC 311 Open Data, APIs & Digital Roadmap here: http://www1.nyc.gov/nyc-
resources/categories/civic-services/open-data-apis-digital-roadmap/index.page
2. Then I clicked the NYC311 OpenData: http://www1.nyc.gov/nyc-resources/service/7024/
nyc311-opendata
3. Then I got the 311 Service Requests from 2010 to Present here: https://
data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-
nwe9
4. And got the API documents here: https://dev.socrata.com/foundry/data.cityofnewyork.us/
fhrw-4uyv
5. And I tried the API URL queries with different parameters in my Chrome.


Before I found the NYC311 Open Data API, I wanted to choose the NYC311 Content API(https://developer.cityofnewyork.us/api/open311-inquiry), which supplies access to theinformation about government services and facilities. I registered as a user, created a project and got an APP ID and key. We could use this API to get the service list, service information, facilities list and information, frequently asked questions list and information and 311 today feed which provides daily status messages regarding public schools, alternate side parking and garbage/recycling pick up, which are also useful. However I didn’t find any entrance for me to change them into custom queries. So I switched my API to NYC 311 service requests API to get the customized queries.
