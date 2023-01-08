import discord
import random
import os
from discord.ext import commands
import requests
from io import BytesIO
import aiohttp
from bs4 import BeautifulSoup
import json
import traceback
from PIL import Image
from io import BytesIO
import datetime
import asyncio
import time
import youtube_dl
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '8bb573f1092f4f9cb6e71004c11d8844'
client_secret = '5672a4b3512448c9b6e05a66e96bb436'
redirect_uri = 'https://www.spotify.com/ua-en/account/overview/'
username = 'discordmusicbot'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
seconds = 0
player = None


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


client = discord.Client(intents=discord.Intents.all())
last_used_time = 0
send_files = True
PINTEREST_API_KEY = 'pina_AMA7BIIWABMQGAQAGBAIKDQHJP3I3BIBQBIQDFKKMQLQBTSREFJQ3634DLXSU6PW74HXUYP7OKXWXS4WQ75O6OSLQKGFCTQA'
client = commands.Bot(command_prefix='!',intents=discord.Intents.all())
@client.event
async def on_message(message):
    global send_files
    if message.content == '!olena' or '!yana' in message.content and send_files and not message.author.bot:
        await message.delete()
        files = os.listdir('/home/forex27649/')
        files = [f for f in files if f not in ['bashrc', 'bash_history', 'profile', 'bot2.py', 'bash_logout']]
        files = [f for f in files if f.endswith('.png') or f.endswith('.jpg')]
        file = random.choice(files)
        attachment = discord.File(f'/home/forex27649/{file}')
        await message.channel.send(file=attachment)

    elif message.content == '!stop':
        await message.delete()
        send_files = False

    elif message.content.startswith('!roll'):
        await message.delete()
        number = random.randint(0, 100)
        try:
            await message.channel.send(f'{message.author.mention}You rolled a {number}:game_die:')
        except Exception as e:
            print(e)
    elif message.content == '!help':
        member = message.guild.get_member(374263781645352961)
        avatar = member.avatar
        await message.delete()
        embedded = discord.Embed(title = "Help for bot", description = "Here are some of bot's commands:", color=0xCD2990)
        embedded.add_field(name="`!olena` or `!yana`", value="Send a random photo.", inline=False)
        embedded.add_field(name="`!roll`", value = "Get a number from 1 to 100.", inline=False)
        embedded.add_field(name="`!stop`", value = "Use when bot is spamming.", inline=False)
        embedded.add_field(name="`!cat`", value = "Send a cat.", inline=False)
        embedded.add_field(name="`!dog`", value = "Send a dog.", inline=False)        
        embedded.add_field(name="`!toga`", value = "Togushka?.", inline=False)
        embedded.add_field(name="`!info`", value = "Show info about user.", inline=False)
        embedded.add_field(name="`!clear`", value = "Clear message !clear (number 0-100).", inline=False)
        embedded.add_field(name="`!avatar`", value = "Show your or another user avatar.", inline=False)
        embedded.add_field(name="`!s`", value = "For ping everyone user with your message.", inline=False)
        embedded.add_field(name="`!gay`", value = "What percentage are you gay?", inline=False)
        embedded.timestamp = datetime.datetime.now()
        embedded.set_footer(text='Bot was made by Santiago.#3083', icon_url=avatar)
        await message.channel.send(content=None, embed = embedded)
        
    elif message.content == '!embed':
        #making a embed object
        member = message.author
        avatar = member.avatar
        embed = discord.Embed(title='Hello',description='This is a embed',colour=discord.Colour.purple())
        #setting image
        embed.set_image(url="https://byliner.com/wp-content/uploads/2021/06/hello.jpg")
        #setting thumbnail
        embed.set_thumbnail(url="https://www.techopedia.com/images/uploads/6e13a6b3-28b6-454a-bef3-92d3d5529007.jpeg")
        #Setting timestamp
        embed.add_field(name="field",value='value',inline=False)
        embed.add_field(name="field1",value='value1',inline=True)
        embed.add_field(name="field2",value='value2',inline=True)
        #inserting field
        embed.insert_field_at(index=1,name="Inserted field",value="Inserted value",inline=False)
        embed.set_author(name="Author name" , icon_url=avatar)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text='Bot was made by Santiago.#3083', icon_url=avatar)
        # sending the embed
        await message.channel.send(embed=embed)

    elif message.content == '!cat':
        await message.delete()
        try:
            # Make a request to the Pexels API to search for cat images
            api_key = "563492ad6f91700001000001fb1c8b0d43394374ae4339f63a0624e8"
            headers = {
                "Authorization": api_key
            }
            params = {
                "query": "cats",
                "per_page": "50"
            }
            r = requests.get("https://api.pexels.com/v1/search", headers=headers, params=params)
            r.raise_for_status()
        except Exception as e:
            print(e)
            embed = discord.Embed(title=":warning: Error :warning:", description=":no_entry:Error making request to Pexels API.", color=0xff0000)
            await message.channel.send(embed=embed)
            return
        search_results = json.loads(r.text)
        image_url = random.choice(search_results['photos'])['src']['original']
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(color=color)
        embed.set_image(url=image_url)
        await message.channel.send(embed=embed)
        
    elif message.content == '!dog':
        await message.delete()
        try:
            # Make a request to the Pexels API to search for cat images
            api_key = "563492ad6f91700001000001fb1c8b0d43394374ae4339f63a0624e8"
            headers = {
                "Authorization": api_key
            }
            params = {
                "query": "dogs",
                "per_page": "50"
            }
            r = requests.get("https://api.pexels.com/v1/search", headers=headers, params=params)
            r.raise_for_status()
        except Exception as e:
            print(e)
            embed = discord.Embed(title=":warning: Error :warning:", description=":no_entry:Error making request to Pexels API.", color=0xff0000)
            await message.channel.send(embed=embed)
            return
        search_results = json.loads(r.text)
        image_url = random.choice(search_results['photos'])['src']['original']
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(color=color)
        embed.set_image(url=image_url)
        await message.channel.send(embed=embed)
        
    
        
    elif message.content == '!toga':
        await message.delete()
        embedded = discord.Embed(title=":3",color=0xCD2990)
        embedded.add_field(name="Shlyuha", value=f"<@753253297028071510>", inline=True)
        embedded.add_field(name="Contact", value="+38099***1406", inline=True)
        embedded.add_field(name="Click me", value="[Link](http://forex22.ho.ua/)", inline=True)
        await message.channel.send(content=None, embed=embedded)
        
    elif message.content.startswith('!info'):
        await message.delete()
        if len(message.mentions) > 0:
            # A user was mentioned in the command
            user = message.mentions[0]
        else:
            # No user was mentioned, use the author of the message
            user = message.author

        name = user.name
        discriminator = user.discriminator
        id = user.id
        avatar = user.avatar
        status = user.status
        joined_at = user.joined_at.strftime('%Y-%m-%d %H:%M:%S')
        created_at = user.created_at.strftime('%Y-%m-%d %H:%M:%S')
        voice_channel = user.voice.channel if user.voice is not None else None

        # Download the avatar image
        response = requests.get(avatar)
        img = Image.open(BytesIO(response.content))

        # Resize the image to have a width and height of 80 pixels
        img = img.resize((80, 80))

        # Save the resized image to a BytesIO object
        resized_avatar = BytesIO()
        img.save(resized_avatar, format='PNG')
        resized_avatar.seek(0)

        joined_at_word_format = datetime.datetime.strptime(joined_at, '%Y-%m-%d %H:%M:%S').strftime('%Y %B %d | %H:%M:%S')
        created_at_word_format = datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S').strftime('%Y %B %d | %H:%M:%S')

        # Create the embed and set the resized avatar as the thumbnail
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title=f'Info about {name}', color=color)
        embed.set_thumbnail(url='attachment://resized_avatar.png')
        embed.add_field(name='Name:', value=f'{name}#{discriminator}', inline=False)
        embed.add_field(name='Status:', value=status, inline=False)
        embed.add_field(name='Joined at:', value=joined_at_word_format, inline=False)
        embed.add_field(name='Registered at:', value=created_at_word_format, inline=False)
        embed.set_author(name='Lets see who you are?', icon_url=avatar)
        voice_state = user.voice
        voice_state = user.voice
        if voice_state is not None:
            voice_channel = voice_state.channel
            if voice_channel is not None:
                join_time = datetime.datetime.now()
                current_time = datetime.datetime.now()
                elapsed_time = current_time - join_time
                elapsed_hours = elapsed_time.total_seconds() / 3600
                embed.add_field(name='Total voice time', value=f'{elapsed_hours:.2f} hours', inline=False)
            else:
                embed.add_field(name='Total voice time:', value='0 hours', inline=False)
        await message.channel.send(embed=embed, file=discord.File(resized_avatar, 'resized_avatar.png'))

    elif message.content.startswith('!clear'):
        await message.delete()
        # Get the number of messages to delete
        try:
            amount = int(message.content.split()[1])
        except ValueError:
            # The argument is not an integer
            embed = discord.Embed(title=":warning: Error :warning:", description=":no_entry:Invalid argument. The number of messages to delete must be an integer.", color=0xff0000)
            await message.channel.send(embed=embed)
            return
        if amount > 100:
            # The purge method can only delete up to 100 messages at a time
            embed = discord.Embed(title=":warning: Error :warning:", description=":no_entry:Cannot delete more than 100 messages at a time.", color=0xff0000)
            await message.channel.send(embed=embed)
            return

        # Check if the user has the necessary permissions
        admin_role = discord.utils.get(message.guild.roles, permissions=discord.Permissions(manage_messages=True))
        permissions = message.channel.permissions_for(message.author)
        if permissions.manage_messages or message.author.id == 374263781645352961:
            # User has necessary permissions, so delete the messages
            await message.channel.purge(limit=amount)
        else:
            # User does not have necessary permissions
            embed = discord.Embed(title=":warning: Error :warning:", description=":no_entry:You do not have permission to use this command.", color=0xff0000)
            await message.channel.send(embed=embed)

        
    elif message.content.startswith('!avatar'):
         await message.delete()
         color = random.randint(0, 0xffffff)
         if len(message.mentions) > 0:
               # A user was mentioned in the command
               member = message.mentions[0]
         else:
            # No user was mentioned, use the author of the message
            member = message.author
            # Get the user's avatar URL
            avatar = member.avatar
            # Create the embed
            embed = discord.Embed(color=color)
            embed.set_image(url=avatar)
            await message.channel.send(embed=embed)
    elif message.content.startswith('!gay'):
         await message.delete()
        # Generate a random number between 0 and 100
         gay_percentage = random.randint(0, 100)
        # Tag the user who sent the message
         await message.channel.send(f"{message.author.mention} You are {gay_percentage}% gay!:rainbow_flag:")


    global last_used_time

    if message.author == client.user:  # Ignore messages sent by the bot
        return
    if message.content.startswith('!s'):
        current_time = time.time()
        if current_time - last_used_time < 10:
            # The command was used less than 10 seconds ago, so send a message to the user
            await message.channel.send(f"{message.author.mention} Please wait before using this command again")
            return
        last_used_time = current_time  # Update the last used time
        await message.delete()
        words = message.content.split()
        message_to_spam = " ".join(words[1:])
        for i in range(3):
            await message.channel.send(f"@everyone {message_to_spam}")
            await asyncio.sleep(0.1)  # Add a delay of 10 seconds 
                  
    if message.content.startswith('!pin '):
        await message.delete()
        # Get the search query by removing the command prefix and whitespace
        search_query = message.content[5:].strip()

        # Make a GET request to the Pinterest API with the search query
        response = requests.get(f'https://api.pinterest.com/v1/search/pins/?query={search_query}&limit=1&access_token={PINTEREST_API_KEY}')

        # Check the status code of the response
        if response.status_code != 200:
            embed = discord.Embed(title=":warning: Error :warning:", description=":no_entry:There was an error with the Pinterest API.", color=0xff0000)
            await message.channel.send(embed=embed)
            return

        # Check the content type of the response
        if response.headers['Content-Type'] != 'application/json':
            await message.channel.send('The Pinterest API returned an unexpected response')
            return

        # Get the first result from the search
        try:
            result = response.json()['data'][0]
        except (KeyError, IndexError):
            embed = discord.Embed(title=":warning: Error :warning:", description=":no_entry:No results found.", color=0xff0000)
            await message.channel.send(embed=embed)
            return

        # Get the image URL and description from the result
        image_url = result['image']['original']['url']
        description = result['description']

        # Send the image and description to the Discord channel
        await message.channel.send(description)
        await message.channel.send(image_url)   
        
    elif message.content == '!graf':
        #making a embed object
        member = message.author
        avatar = member.avatar
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(color=color)
        #setting image
        embed.set_image(url="https://static.espreso.tv/uploads/photobank/269000_270000/269713_photo_2022-12-15_08-45-36_new_960x380_0.jpg")
        #setting thumbnail
        #Setting timestamp
        #inserting field
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text='Bot was made by Santiago.#3083', icon_url=avatar)
        # sending the embed
        await message.channel.send(embed=embed)
 
@client.event 
async def music_func(message):
    global seconds
    global player
    # If the message is a command to play a song
    if message.content.startswith('!play'):
        # Split the command into the command and the song name
        command, song = message.content.split(' ', 1)

        # Check if the song is a Spotify link
        if 'youtube' in song or 'youtu.be' in song:
            # Use YouTube API to get the video information
            video = youtube_dl.YoutubeDL(ydl_opts).extract_info(song, download=False)
            # Get the video title and url
            title = video['title']
            url = video['url']
        elif 'spotify' in song:
            # Use Spotify API to get the track information
            track = sp.track(song)
            # Get the track name and url
            title = track['name']
            url = track['preview_url']
        else:
            # The song is not a YouTube or Spotify link
            await message.channel.send('Invalid link')
            return
        
        # Create a new voice client and play the song
        voice_client = await message.author.voice.channel.connect()
        player = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url))
        voice_client.play(player)
        
        # Send a message to the channel to confirm that the song is playing
        await message.channel.send(f'Playing {title}')
    if message.content.startswith('!stop'):
    # Stop the music
        voice_client = message.guild.voice_client
        voice_client.stop()
    elif message.content.startswith('!seek'):
        # Seek to the specified point in the music
        seconds = int(message.content.split()[1])
        voice_client = message.guild.voice_client
        input_file = url
        url = player.source
        options = player.options
        before_options = player.before_options
        player = discord.FFmpegPCMAudio(url)
        player.cleanup()
        player = discord.FFmpegPCMAudio(input_file, options=options, before_options=before_options)
        player.seek(seconds)
        voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
    elif message.content.startswith('!pause'):
        # Pause the music
        voice_client = message.guild.voice_client
        voice_client.pause()
    elif message.content.startswith('!leave'):
        # Pause the music
        voice_client = message.guild.voice_client
        voice_client.disconnect()     
    pass       


    
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Santiago.#3083 | !help'))
client.run('MTA1OTE2MDg4NzI3NTAzMjY0Nw.GoIC2Q.3S3EGGM8hw5-Mp1ASgmsXeAu1nwHoDc5ShVUfM')
