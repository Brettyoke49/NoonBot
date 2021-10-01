# bot.py
import os
import discord
from Commands import Command
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f'{client.user} has connected to {guild.name}(id: {guild.id})!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content[0] == '!':
        commandHandler = Command(message.content)
        response = commandHandler.execute()
        await message.channel.send(response)

client.run(TOKEN)