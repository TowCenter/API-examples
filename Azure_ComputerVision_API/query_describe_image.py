"""
Describe Image - Sample Query

The describe image query is a POST request that takes in an image URL or a raw image binary through
the request body and are returns a readable text description of the image along with a collection
of content tags.

Make sure to replace the {KEY_1} placeholder with your KEY 1 security key.

curl -X POST \
  'https://eastus.api.cognitive.microsoft.com/vision/v2.0/describe?maxCandidates=2' \
  -H 'Content-Type: application/json' \
  -H 'Ocp-Apim-Subscription-Key: {KEY_1}' \
  -H 'cache-control: no-cache' \
  -d '{
    "url":"https://journalism.columbia.edu/files/soj/styles/flex_full/public/content/image/2018/09/dsc_7432_0.jpg"
}'
"""

import requests

url = "https://eastus.api.cognitive.microsoft.com/vision/v2.0/describe"

querystring = {"maxCandidates":"2"}

payload = "{\n\t\"url\":\"https://journalism.columbia.edu/files/soj/styles/flex_full/public/content/image/2018/09/dsc_7432_0.jpg\"\n}"
headers = {
    'Ocp-Apim-Subscription-Key': '{KEY 1}',
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
