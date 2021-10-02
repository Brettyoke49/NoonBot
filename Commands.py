from Roll import Roll
from Kick import Kick

class Command:
    def help(arg1, arg2):
        return """Commands & syntax:
```!Roll [Low] [High]   - Roll a number between low and high. Default low and high are 1 through 100"
!Kick [User]         - Kick a given user. Use this wisely
!AddRole [Role]      - Add the specified role to yourself
!RemoveRole [Role]   - Remove the specified role from yourself```"""

    def invalid(arg1, arg2):
        return "Invalid command"

    def __init__(self, message, user, mention):
        self.parsedMessage = message.split()
        self.parsedMessage[0] = self.parsedMessage[0].upper()
        self.sendingUser = user
        self.sendingUserMention = mention

    _commands = {
            '!HELP' : help,
            '!ROLL' : Roll.roll,
            '!KICK' : Kick.kick,
            '!ADDROLE' : "This command is not yet functional...",
            '!REMOVEROLE' : "This command is not yet functional..."}

    sendingUser = ""
    sendingUserMention = ""
    parsedMessage = []

    def execute(self):
        return self._commands.get(self.parsedMessage[0], self.invalid)(self.parsedMessage, self.sendingUserMention)