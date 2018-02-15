import os

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# The SECRET_KEY variable stores name of the file with client_id and client_secret.
SECRET_KEY = "client_secret.json"

# OAuth 2.0 access scope allows for full read/write access to the authenticated user's account
SCOPE = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(SECRET_KEY, SCOPE)
  credentials = flow.run_console()
  return build(API_SERVICE, API_VERSION, credentials = credentials)

def channels_list_by_username(service, **kwargs):
  results = service.channels().list(**kwargs).execute()
  
  print('This channel\'s ID is %s. Its title is %s, and it has %s views.' %
       (results['items'][0]['id'],
        results['items'][0]['snippet']['title'],
        results['items'][0]['statistics']['viewCount']))

if __name__ == '__main__':
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  service = get_authenticated_service()
  channels_list_by_username(service,part='snippet,contentDetails,statistics',forUsername='Vevo')