# bot.py
import os
from dotenv import load_dotenv
import datetime
from pytz import timezone

from discord.ext import tasks, commands
import discord

from Roll import Roll
from Roles import Roles

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
ERRORS_CHANNEL = int(os.getenv('ERRORS_CHANNEL'))

myHelpCommand = commands.DefaultHelpCommand(
    no_category = "\nOther Commands"
)

bot = commands.Bot(
    command_prefix='!', 
    case_insensitive=True, 
    help_command = myHelpCommand
)

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(f'{bot.user.name} has connected to {guild.name}(id: {guild.id})!')

#Roll
@bot.command(name = "Roll", help = "[Low] [High] - Roll a number from low to high. Default is 1-100")
async def _roll(ctx, low: int=None, high: int=None):
    roller = Roll(ctx.author.mention)
    message = roller.roll(low, high)
    if message != None:
        await ctx.send(message)

#Kick
@bot.command(name = "Kick", help = "[User] - Kick a given user. Use this wisely")
async def _kick(ctx, member: discord.Member):
    await ctx.send("Hey everyone! " + ctx.author.mention + " just tried to kick " + member.mention + "! What a bastard!")

class RoleEditing(commands.Cog, name = "Role Editing"):
    """Contains all commands relevant to role manipulation"""
    def __init__(self, bot):
        self.bot = bot

    #Add Role
    @commands.command(name = "AddRole", help = "[Role] - Add the specified role to yourself")
    async def _addRole(self, ctx, role: discord.Role):
        roleManager = Roles(ctx.author)
        message = await roleManager.addRole(role)
        await ctx.send(message)

    #Remove Role
    @commands.command(name = "RemoveRole", help = "[Role] - Remove the specified role from yourself")
    async def _removeRole(self, ctx, role: discord.Role):
        roleManager = Roles(ctx.author)
        message = await roleManager.removeRole(role)
        await ctx.send(message)

    #List My Roles
    @commands.command(name = "MyRoles", help = "List all of your current roles")
    async def _myRoles(self, ctx):
        roleManager = Roles(ctx.author)
        message = roleManager.listRoles()
        await ctx.send(message)

    #List All Roles
    @commands.command(name = "AllRoles", help = "List all of the server roles")
    @commands.cooldown(1, 10, commands.BucketType.channel)
    async def _allRoles(self, ctx):
        roleManager = Roles(ctx.author)
        message = roleManager.listServerRoles()   
        await ctx.send(message)

#COMMAND ERROR HANDLER
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.RoleNotFound):
        await ctx.send("That role doesn't exist, check your capitalization")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permissions to add that role")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("That member doesn't exist")
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds.")
    elif isinstance(error, commands.UserInputError):
        await ctx.send("Invalid input for that command")
    else:
        est = timezone('US/Eastern')
        message = str(datetime.datetime.now(est)) + " - message: " + ctx.message.content + "\nError(s):" + ', '.join(error.args)
        errorChannel = bot.get_channel(ERRORS_CHANNEL)
        await errorChannel.send(message)

bot.add_cog(RoleEditing(bot))
bot.run(TOKEN)