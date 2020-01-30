"""
OCR - Sample Query

The OCR query is a POST request that takes in an image URL or a raw image binary data through the
request body and returns the words recognized in order with bounding box information.

Make sure to replace the {KEY_1} placeholder with your KEY 1 security key.

curl -X POST \
  'https://eastus.api.cognitive.microsoft.com/vision/v1.0/ocr?language=en&detectOrientation=true' \
  -H 'Content-Type: application/json' \
  -H 'Ocp-Apim-Subscription-Key:{KEY_1}' \
  -H 'cache-control: no-cache' \
  -d '{
    "url":"http://www.techmynd.com/wp-content/uploads/2009/11/upside-down.jpg"
}'
"""

import requests

url = "https://eastus.api.cognitive.microsoft.com/vision/v1.0/ocr"

querystring = {"language":"en","detectOrientation":"true"}

payload = "{\n\t\"url\":\"http://www.techmynd.com/wp-content/uploads/2009/11/upside-down.jpg\"\n}"
headers = {
    'Ocp-Apim-Subscription-Key': '{KEY 1}',
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
