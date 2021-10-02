import os
from discord.ext import tasks, commands
import discord

class Roles:
    member: discord.Member = None

    def __init__(self, member):
        self.member = member

    async def addRole(self, role):
        if role in self.member.roles:
            return f"{self.member.mention} already has role {role}"
        else:
            try:
                await self.member.add_roles(role)
                return f"Added {role} role to {self.member.mention}"
            except:
                return f"Failed to add {role} role to {self.member.mention}"

    async def removeRole(self, role):
        if role not in self.member.roles:
            return f"{self.member.mention} does not have role {role}"
        else:
            try:
                await self.member.remove_roles(role)
                return f"Removed {role} role from {self.member.mention}"
            except:
                return f"Failed to remove {role} role from {self.member.mention}."

    def listRoles(self):
        roles = ""
        delimiter = ""

        for role in self.member.roles:
            if role.name == "@everyone": 
                continue
            roles += delimiter + role.name
            delimiter = ", "

        return f"Your roles: {roles}"