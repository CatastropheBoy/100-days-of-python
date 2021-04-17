from bs4 import BeautifulSoup
import requests
import spotipy
import pprint
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = "e06cd029c8c14d7f803b39c2518355f3"
SPOTIFY_SECRET = "PLACEHOLDER"
REDIRECT_URI = "http://example.com"
scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID, 
        client_secret=SPOTIFY_SECRET, 
        redirect_uri=REDIRECT_URI, 
        scope=scope))

sp.current_user()



date = input("Enter a date to view: YYYY-MM-DD")

url = f"https://www.billboard.com/charts/hot-100/{date}"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, "html.parser")

song_titles = [song.getText() for song in soup.find_all(name="span", class_="chart-element__information__song")]
print(song_titles)

sp.user_playlist_create("professor_k", date, False, False, f"Billboard top 100 songs for {date}")
tracks = []

year = date.split("-")[0]
for song in song_titles:
    search = sp.search(f"track:{song} year:{year}", type="track", limit=1)
    try:
        tracks.append(search["tracks"]["items"][0]["id"])
    except:
        print(f"Couldn't find {song}, skipping.")


sp.user_playlist_add_tracks("professork", "3W8Yv5tOTOAFBB5LzTnqdF", tracks)