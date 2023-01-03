import discord
import random
import os

client = discord.Client(intents=discord.Intents.all())

send_files = True

@client.event
async def on_message(message):
    global send_files
    if message.content == '/olena' or '/yana' in message.content and send_files and not message.author.bot:
        await message.delete()
        files = os.listdir('C:/Users/Sanya/Desktop/kolegy/')
        file = random.choice(files)
        attachment = discord.File(f'C:/Users/Sanya/Desktop/kolegy/{file}')
        await message.channel.send(file=attachment)
        
    elif message.content == '/stop':
        send_files = False
        
    elif message.content.startswith('/roll'):
        number = random.randint(0, 100)
        try:
            await message.channel.send(f'You rolled a {number}')
        except Exception as e:
            print(e)

client.run('MTA0NDYzMTg1MzU0MzQ3NzI0OA.GVEIJQ.SbC8Bj2TKn52kuVjfV5UT8P7x34qXoZ-b4y_DM')
