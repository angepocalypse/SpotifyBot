# -*- coding: utf-8 -*-

import discord
import os
import aiohttp
import json
import logging
import sys

from common.SearchSpotify import search_and_generate
from common.SearchYoutube import get_title
from conf.config import Config
from datetime import datetime
from discord.ext import commands
from discord.utils import get


client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    logging.info('Bot is ready')


@client.command()
async def ping(ctx):
    ''' Basic ping pong function  '''

    logging.info("Ping command triggered by {}".format(
        ctx.author.display_name))
    await ctx.send('Pong!')


@client.command(aliases=['playlist'])
async def search_for_music(ctx, playlist_name=None):
    ''' Returns Spotify playlist with all youtube title queries found in channel '''

    logging.info("Playlist command triggered by {}".format(
        ctx.author.display_name))
    await ctx.send('Searching for tunes...')

    if not playlist_name:
        playlist_name = "SpotifyBot {}".format(
            datetime.now().strftime("%c"))

    query_list = []
    history = ctx.channel.history(limit=None)

    async for elem in history:
        if "youtube.com" in elem.clean_content:
            yt_url = elem.clean_content
            logging.debug("Youtube url: {}".format(yt_url))
            title = get_title(yt_url)
            if title is not None:
                # debug compare discord embedded link info to searching youtube and getting title
                logging.debug("Embedded element title: {}".format(
                    elem.embeds[0].title))
                logging.debug("Search youtube title: {}".format(title))

                query_list.append(title)

    logging.debug(query_list)

    # Pass query list to spotipy function
    playlist_url = search_and_generate(query_list, playlist_name)
    await ctx.send(playlist_url)


def main():
    logging.basicConfig(filename='spotifyBot.log', level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())


if __name__ == "__main__":
    with open('config.json', 'r') as read_file:
        data = json.load(read_file)

    main()
    TOKEN = Config.TOKEN
    logging.info('Starting Client...')
    client.run(TOKEN)
