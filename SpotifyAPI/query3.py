#####
# query3.py
# Returns audio analysis of a track
# Adapted from: https://github.com/plamere/spotipy/blob/master/examples/audio_analysis_for_track.py
#####

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys

# Access tokens
client_id = "[client ID]"
client_secret = "[client secret]"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Hard-coding the track to be "The Present Tense," by Radiohead
track_id = 'spotify:track:4eruRiSfDY1jdT03hjyi0i'

# Get audio analysis from API
analysis = sp.audio_analysis(track_id)

# Print analysis
print(json.dumps(analysis, indent=4))