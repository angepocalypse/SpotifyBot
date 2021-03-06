# SpotifyBot
SpotifyBot for Discord. Scans through current channel's history for youtube links, then searches spotify for song titles and creates a playlist.


## Setup
Create a virtual environment then install requirements:
```bash
virtualenv .venv

.venv\Scripts\activate

(.venv) pip3 install -r requirements.txt
```
Edit the config.json file with your Discord Bot token and Spotify API Credentials.
```bash
{
    "Discord": {
      "TOKEN": "{Your Discord Bot Token}"
    },
    "Spotify": {
      "SPOTIPY_CLIENT_ID": "{Your Spotipy client id}",
      "SPOTIPY_CLIENT_SECRET": "{Your Spotipy client secret}",
      "REDIRECT_URI": "http://localhost:8080/",
      "SCOPE": "playlist-modify-public",
      "USERNAME": "{Username for spotify account}"
    }
}
  
```

## Run Discord Bot
```bash
python SpotifyBot.py
```