
# Spotify Playlist Freezer

## Problem Description
Spotify provides dynamic playlists that are generated based on user's listening habits. These dynamic playlists are unique to each user and change over time. However, sharing these dynamic playlists with friends can lead to different song lists due to the personalization.

This script solves the problem by generating a static version of the dynamic playlist. This static playlist can be shared with friends and will not change over time, providing a consistent song list for everyone.

## Usage

### Pre-requisites
- Python installed
- A Spotify developer account
- Client ID and Client Secret from your Spotify app
- Your dynamic playlist ID

### Instructions
1. Clone or download this repository to your local machine.

2. Install the dependencies. This script requires `spotipy`, a lightweight Python library for the Spotify Web API. You can install it with pip:

    ```bash
    pip install spotipy
    ```

3. Set your Spotify API credentials as environment variables. These are used for authenticating with the Spotify API. 

    ```bash
    export SPOTIPY_CLIENT_ID='your-spotify-client-id'
    export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
    ```

4. Run the script from your terminal with the dynamic playlist ID and the desired name for the new static playlist as arguments:

    ```bash
    python freeze_playlist.py your-playlist-id "Your New Playlist Name"
    ```

    For example:

    ```bash
    python freeze_playlist.py 37i9dQZF1E37KkzBQqMg3b "My Shared Playlist"
    ```

5. The script will print a shareable Spotify link to the new static playlist. Share this link with your friends to let them enjoy the same playlist!
