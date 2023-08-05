import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

new_playlist_name = "Mix BR"
playlist_id = "37i9dQZF1E37KkzBQqMg3b"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("client_id"),
        client_secret=os.getenv("client_secret"),
        redirect_uri="http://127.0.0.1:9090",
        scope="playlist-read-private playlist-modify-public",
    )
)

tracks = sp.playlist_tracks(playlist_id)
user_id = sp.me()["id"]
new_playlist = sp.user_playlist_create(user_id, new_playlist_name)
track_ids = [track["track"]["id"] for track in tracks["items"]]
sp.playlist_add_items(new_playlist["id"], track_ids)
shared_link = new_playlist["external_urls"]["spotify"]
print(f"Shareable link: {shared_link}")
