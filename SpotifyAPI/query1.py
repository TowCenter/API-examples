#####
# query1.py
# Returns a list of top tracks by an artist.
# Adapted from: https://stackoverflow.com/questions/46966932/how-to-work-in-spotify-python-api
#####

import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint

# Access tokens
client_id = "[client ID]"
client_secret = "[client secret]"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Hard-coding the artist to be Radiohead and the 
# country to be the U.S.
artist_id = 'spotify:artist:4Z8W4fKeB5YxbusRsdQVPb'
country = 'US'

# Getting information from the API
results = sp.artist_top_tracks(artist_id=artist_id, country=country)

# Print the top 3 tracks and provide a URL to an mp3 sample
for track in results['tracks'][:3]:
    print ('TRACK: ' + track['name'])
    print ('LINK: ' + track['preview_url'])
    print()