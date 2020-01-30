"""
Analyze Image - Sample Query

The analyze image query is a POST request that takes in an image URL or a raw image binary
through the request body and returns a JSON of image features detected. The image features
detected can be fine-tuned using the visualParams and details request parameters.

Make sure to replace the {KEY_1} placeholder with your KEY 1 security key.

curl -X POST \
  'https://eastus.api.cognitive.microsoft.com/vision/v2.0/analyze?visualFeatures=adult,faces&details=celebrities' \
  -H 'Content-Type: application/json' \
  -H 'Ocp-Apim-Subscription-Key: {KEY_1}' \
  -H 'cache-control: no-cache' \
  -d '{
    "url":"https://fm.cnbc.com/applications/cnbc.com/resources/img/editorial/2018/07/16/105332385-1531754604468rtx6bmp1.530x298.jpg?v=1531754709"
}'
"""
import requests

url = "https://eastus.api.cognitive.microsoft.com/vision/v2.0/analyze"

querystring = {"visualFeatures":"adult,faces","details":"celebrities"}

payload = "{\n\t\"url\":\"https://fm.cnbc.com/applications/cnbc.com/resources/img/editorial/2018/07/16/105332385-1531754604468rtx6bmp1.530x298.jpg?v=1531754709\"\n}"
headers = {
    'Ocp-Apim-Subscription-Key': '{KEY_1}'},
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
