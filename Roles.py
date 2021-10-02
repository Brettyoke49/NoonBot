from discord.ext import tasks, commands
import discord

class Roles:
    member

    def __init__(self, member):
        self.member = member

    def addRole(self, role):
        return "add"

    def removeRole(self, role):
        return "remove"

    def listRoles(self):
        return "list"