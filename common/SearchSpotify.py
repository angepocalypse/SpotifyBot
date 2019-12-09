# -*- coding: utf-8 -*-

import json
import logging
import sys
import re
import spotipy
import spotipy.util as util
import spotipy.oauth2 as oauth2

from conf.config import Config


def better_search_term(query):
    ''' Removes certain known situations that would result in a bad spotify search '''

    # get first half of string if there's any parens
    query = query.split('(')[0]

    # get first half of string if "cover" in name
    query = query.split('Cover')[0]

    # get first half of string if there's any brackets
    query = query.split('[')[0]

    # remove "&""
    query = query.replace(' & ', '  ')

    # remove "ft.""
    query = re.sub(" ft. ", " ", query, flags=re.I)

    # remove digits
    query = ''.join([i for i in query if not i.isdigit()])

    # remove "live" because not all live versions are on spotify
    query = re.sub(" live ", " ", query, flags=re.I)

    # remove the word "by"
    query = query.replace(' by ', ' ')

    return query


def search_and_generate(query_list, playlist_name):
    config = Config()
    token = util.prompt_for_user_token(
        username=config.USERNAME,
        scope=config.SCOPE,
        client_id=config.SPOTIPY_CLIENT_ID,
        client_secret=config.SPOTIPY_CLIENT_SECRET,
        redirect_uri=config.REDIRECT_URI)

    spotify = spotipy.Spotify(auth=token)

    tracks = []
    result_dict = {}

    for query in query_list:

        new_query = better_search_term(query)

        results = spotify.search(q=new_query, type='track')
        items = results['tracks']['items']
        if len(items) == 0:
            logging.info("No results for search query: {}".format(query))
            result_dict[query] = {new_query: ""}
            continue

        track = items[0]

        query_dict = {
            'name': track['name'],
            'artist': track['artists'][0]['name']
        }

        result_dict[query] = {new_query: query_dict}

        print(track['name'], track['artists'][0]['name'])
        logging.info("{}: {}".format(track['artists'][0]['name'], track['name']))
        track_uri = track['uri']
        tracks.append(track_uri)
    
    logging.debug(result_dict)

    playlist = spotify.user_playlist_create(
        config.USERNAME, playlist_name)

    spotify.user_playlist_add_tracks(
        config.USERNAME, playlist['id'], tracks)

    playlist_url = playlist['external_urls']['spotify']

    return playlist_url
