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
async def on_message(message: discord.Message):
    if message.author == client.user or message.content[0] != '!':
        return
    commandHandler = Command(message.content, message.author.display_name, message.author.mention)
    response = commandHandler.execute()
    await message.channel.send(response)

client.run(TOKEN)