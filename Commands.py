class Command:
    commands = {
            '!HELP' : 
"""Commands & syntax:
```!Roll [Low] [High]   - Roll a number between low and high. Default low and high are 1 through 100"
!Kick [User]         - Kick a given user. Use this wisely
!AddRole [Role]      - Add the specified role to yourself
!RemoveRole [Role]   - Remove the specified role from yourself```""",
            '!ROLL' : "@x rolled i-j: #",
            '!KICK' : "Hey everyone! @x just tried to kick @y! That bastard!",
            '!ADDROLE' : "This command is not yet functional...",
            '!REMOVEROLE' : "This command is not yet functional..."}

    sendingUser = ""
    sendingUserMention = ""
    parsedMessage = []

    def __init__(self, message, user, mention):
        self.parsedMessage = message.split()
        self.parsedMessage[0] = self.parsedMessage[0].upper()
        self.sendingUser = user
        self.sendingUserMention = mention

    def execute(self):
        return self.commands.get(self.parsedMessage[0], "Invalid command")