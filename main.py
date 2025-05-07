import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import matplotlib.pyplot as plt
import pandas as pd

# Load .env file
load_dotenv()

# Now get variables from the environment
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

# Initialize Spotify API with environment-based credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="user-library-read user-top-read"
))

# Fetch Top Tracks (Top 5)
top_tracks = sp.current_user_top_tracks(limit=5, time_range='medium_term')  # 'short_term', 'medium_term', or 'long_term'

print("Your Top 5 Tracks:")
for idx, track in enumerate(top_tracks['items']):
    print(f"{idx + 1}. {track['name']} by {track['artists'][0]['name']}")

# Fetch Top Artists (Top 5)
top_artists = sp.current_user_top_artists(limit=5, time_range='medium_term')

# Prepare data for plotting
artists = [artist['name'] for artist in top_artists['items']]
popularity = [artist['popularity'] for artist in top_artists['items']]

# Create a bar plot for Top Artists based on popularity
plt.barh(artists, popularity)
plt.xlabel('Popularity')
plt.title('Your Top 5 Artists')
plt.show()

import pandas as pd

# Prepare DataFrame for Top Tracks
tracks_data = {
    'Track': [track['name'] for track in top_tracks['items']],
    'Artist': [track['artists'][0]['name'] for track in top_tracks['items']],
    'Popularity': [track['popularity'] for track in top_tracks['items']]
}
tracks_df = pd.DataFrame(tracks_data)

# Save to CSV
tracks_df.to_csv('top_tracks.csv', index=False)

print("\nYour Top 5 Artists:")
for idx, artist in enumerate(top_artists['items']):
    print(f"{idx + 1}. {artist['name']} with popularity {artist['popularity']}")

