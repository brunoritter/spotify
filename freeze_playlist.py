import spotipy
import argparse
from spotipy.oauth2 import SpotifyOAuth


def create_playlist(playlist_id, new_playlist_name):
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create a new playlist from an existing playlist ID."
    )
    parser.add_argument(
        "playlist_id", type=str, help="The ID of the existing playlist."
    )
    parser.add_argument(
        "new_playlist_name", type=str, help="The name for the new playlist."
    )

    args = parser.parse_args()
    create_playlist(args.playlist_id, args.new_playlist_name)
