import json

class Config(object):
    with open("config.json", "r") as read_file:
        data = json.load(read_file)

    sp_config = data['Spotify']

    SPOTIPY_CLIENT_ID = sp_config['SPOTIPY_CLIENT_ID']
    SPOTIPY_CLIENT_SECRET = sp_config['SPOTIPY_CLIENT_SECRET']
    REDIRECT_URI = sp_config['REDIRECT_URI']
    SCOPE = sp_config['SCOPE']
    USERNAME = sp_config['USERNAME']

    disc_config = data['Discord']

    TOKEN = disc_config['TOKEN']