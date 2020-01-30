Eugene M. Joseph  
emj2152

## Investigative Techniques
### Assignment 2: API Profile Process Log  

* Decided to profile Microsoft's computer vision API which I'd come across a few years ago when investigating ways to detect and prevent the display of adult content in user-generated images for a platform I was building.

* Googled `microsoft computer vision API` and clicked on the first result which led to this url: `https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/`

* Clicked on the API link which led to the following page: `https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa`

* Looked over the different endpoints and decided to document the **Analyze Image**, **Describe Image**, and **OCR** API endpoints. Also took note of the various parameters for each of the routes.

* Went back to the Computer Vision [landing page](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/) and clicked on the `Pricing` tab and took note of the pricing information located here: https://azure.microsoft.com/en-us/pricing/details/cognitive-services/computer-vision/

* Went back to the Computer Vision [landing page](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/) and clicked on the `Free account` button to start the account creation process.

* Signed up with my old hotmail email address, verified my account via  email  and also verified the account with my credit card. Also saw there was an [option](https://azure.microsoft.com/en-us/free/students/) for students to create an account without the need for credit card verification.

* Once I had created my account and was logged in I went to the [Azure Portal page](https://portal.azure.com/#home) clicked on the **Cognitive Services** link under Azure services heading up top which took me here: https://portal.azure.com/#blade/HubsExtension/Resources/resourceType/Microsoft.CognitiveServices%2Faccounts

* On this Cognitive Services page I pressed the blue plus button to add a service which took me to another page where I clicked on **Computer Vision** button on the bottom right and created a new instance of the computer vision API under my account.

* On the creation page I named my computer vision instance, chose the `Free Trial` option under the subscription field, chose `East US` (located in Virginia) under the location field and chose the `F0` option which is the free option for the pricing tier field.

* After creating the account I returned to the [Cognitive Services hub page](https://portal.azure.com/#blade/HubsExtension/Resources/resourceType/Microsoft.CognitiveServices%2Faccounts) and clicked on my newly created Computer vision instance which brought up the **Quick Start** page.

* Clicked on the **Keys** link from the Quick Start page to access the security keys for my instance. There are two keys (`KEY 1` and `KEY 2`) provided and we can use either one to access the API. I used my `KEY 1` value for this profile.

* Googled `computer vision API python demo microsoft` and clicked on the first [result](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts/python-analyze) which took me to a tutorial on setting up the API with Python.

* Noted that security keys are passed through requests via the header parameter `Ocp-Apim-Subscription-Key` as indicated in the code example.

* Decided to use [Postman](https://www.getpostman.com/) to test the three API endpoints I described earlier. Made sure to instantiate requests with the proper security key parameter noted above.

* Used Postman's code export functionality to generate cURLs for the example queries shown in API profile document. I'm attaching the cURLs and Python 3 code below if readers want to reproduce them. Make sure to replace the {KEY_1} placeholder with your `KEY 1` security key. Readers can run the cURL commands by pasting them in any terminal utility and pressing enter.

* Googled `microsoft azure why do i have 2 keys vision api` and clicked on the first result which led me [here](https://cognitive.uservoice.com/knowledgebase/articles/1141621-api-translator-text-speech-why-are-there-two). Clicked on the redirect link on that page which took me [here](https://www.microsoft.com/en-us/translator/business/faq/#development). Read up on why there were two security keys provided for the API.

* Googled `azure two access keys?` and clicked on the first result which led me [here](https://blogs.msdn.microsoft.com/mast/2013/11/06/why-does-an-azure-storage-account-have-two-access-keys/). Read more information on why Microsoft Azure provides two access keys to their APIs.


### Analyze Image Endpoint Test Query

Make sure to replace the {KEY_1} placeholder with your `KEY 1` security key.

cURL:
```
curl -X POST \
  'https://eastus.api.cognitive.microsoft.com/vision/v2.0/analyze?visualFeatures=adult,%20faces&details=celebrities' \
  -H 'Content-Type: application/json' \
  -H 'Ocp-Apim-Subscription-Key: {KEY_1}' \
  -H 'cache-control: no-cache' \
  -d '{
	"url":"https://fm.cnbc.com/applications/cnbc.com/resources/img/editorial/2018/07/16/105332385-1531754604468rtx6bmp1.530x298.jpg?v=1531754709"
}'
```

Python:
```
import requests

url = "https://eastus.api.cognitive.microsoft.com/vision/v2.0/analyze"

querystring = {"visualFeatures":"adult,%20faces","details":"celebrities"}

payload = "{\n\t\"url\":\"https://fm.cnbc.com/applications/cnbc.com/resources/img/editorial/2018/07/16/105332385-1531754604468rtx6bmp1.530x298.jpg?v=1531754709\"\n}"
headers = {
    'Ocp-Apim-Subscription-Key': {KEY_1}',
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
```

### Describe Image Endpoint Test Query

Make sure to replace the {KEY_1} placeholder with your `KEY 1` security key.

cURL:
```
curl -X POST \
  'https://eastus.api.cognitive.microsoft.com/vision/v2.0/describe?maxCandidates=2' \
  -H 'Content-Type: application/json' \
  -H 'Ocp-Apim-Subscription-Key: {KEY_1}' \
  -H 'cache-control: no-cache' \
  -d '{
	"url":"https://journalism.columbia.edu/files/soj/styles/flex_full/public/content/image/2018/09/dsc_7432_0.jpg"
}'
```

Python:
```
import requests

url = "https://eastus.api.cognitive.microsoft.com/vision/v2.0/describe"

querystring = {"maxCandidates":"2"}

payload = "{\n\t\"url\":\"https://journalism.columbia.edu/files/soj/styles/flex_full/public/content/image/2018/09/dsc_7432_0.jpg\"\n}"
headers = {
    'Ocp-Apim-Subscription-Key': {KEY_1},
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
```

### OCR Endpoint Test Query

Make sure to replace the {KEY_1} placeholder with your `KEY 1` security key.

cURL:
```
curl -X POST \
  'https://eastus.api.cognitive.microsoft.com/vision/v1.0/ocr?language=en&detectOrientation=true' \
  -H 'Content-Type: application/json' \
  -H 'Ocp-Apim-Subscription-Key:{KEY_1}' \
  -H 'cache-control: no-cache' \
  -d '{
	"url":"http://www.techmynd.com/wp-content/uploads/2009/11/upside-down.jpg"
}'
```

Python:
```
import requests

url = "https://eastus.api.cognitive.microsoft.com/vision/v1.0/ocr"

querystring = {"language":"en","detectOrientation":"true"}

payload = "{\n\t\"url\":\"http://www.techmynd.com/wp-content/uploads/2009/11/upside-down.jpg\"\n}"
headers = {
    'Ocp-Apim-Subscription-Key': {KEY_1},
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
```

### References

* https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/
* https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa`
* https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/
* https://azure.microsoft.com/en-us/pricing/details/cognitive-services/computer-vision/
* https://azure.microsoft.com/en-us/free/students/
* https://eastus.dev.cognitive.microsoft.com/docs/services/56f91f2d778daf23d8ec6739/operations/56f91f2e778daf14a499e1fa
* https://cognitive.uservoice.com/knowledgebase/articles/1141621-api-translator-text-speech-why-are-there-two
* https://blogs.msdn.microsoft.com/mast/2013/11/06/why-does-an-azure-storage-account-have-two-access-keys/
* https://westus.dev.cognitive.microsoft.com/docs/services/56f91f2d778daf23d8ec6739/operations/56f91f2e778daf14a499e1fa
* https://westus.dev.cognitive.microsoft.com/docs/services/56f91f2d778daf23d8ec6739/operations/56f91f2e778daf14a499e1fe
* https://westus.dev.cognitive.microsoft.com/docs/services/56f91f2d778daf23d8ec6739/operations/56f91f2e778daf14a499e1fc
