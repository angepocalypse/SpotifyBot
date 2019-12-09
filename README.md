# SpotifyBot
SpotifyBot for Discord
<<<<<<< HEAD


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
=======
>>>>>>> a5d435f2db21b90305fe5e773b784f2b9b4f6b12
