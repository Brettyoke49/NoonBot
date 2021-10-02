# bot.py
import os
from discord.ext import tasks, commands
import discord
from dotenv import load_dotenv

from Roll import Roll
from Roles import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!', case_insensitive=True)

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(f'{bot.user.name} has connected to {guild.name}(id: {guild.id})!')

@bot.command(name = "Roll", help = "[Low] [High] - Roll a number between low and high. Default is 1 through 100")
async def _roll(ctx, low: int=None, high: int=None):
    roller = Roll(ctx.author.mention)
    message = roller.roll(low, high)
    if message != None:
        await ctx.send(message)

@bot.command(name = "Kick", help = "[User] - Kick a given user. Use this wisely")
async def _kick(ctx, member: discord.Member):
    await ctx.send("Hey everyone! " + ctx.author.mention + " just tried to kick " + member.mention + "! What a bastard!")

@bot.command(name = "AddRole", help = "[Role] - Add the specified role to yourself")
async def _addRole(ctx, role: discord.Role):
    return

@bot.command(name = "RemoveRole", help = "[Role] - Remove the specified role from yourself")
async def _removeRole(ctx, role: discord.Role):
    return

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

bot.run(TOKEN)