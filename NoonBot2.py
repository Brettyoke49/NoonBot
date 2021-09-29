# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

def Commands(input):
    commands = {
    '!Help' : 
"""Commands & syntax:
!Games - List of active games and their IDs for game rolling
!Roll [Low] [High] - Roll a number between low and high. Default low and high are 1 through 100""",
    '!Games' : "Splitgate, Dota 2, Valorant"    
    }
    return commands.get(input, None)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f'{client.user} has connected to {guild.name}(id: {guild.id})!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    response = Commands(message.content)
    if response != None:
        await message.channel.send(response)

client.run(TOKEN)