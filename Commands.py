class Command:
    message = ""

    def __init__(self, message):
        self.message = message

    def execute(self):
        if self.message == "!test":
            return self.message
        else:
            return None

    def execute(self):
        commands = {
            '!Help' : 
"""Commands & syntax:
!Games     - List of active games and their IDs for game rolling
!Roll [Low] [High]     - Roll a number between low and high. Default low and high are 1 through 100"
!Kick [User]     - Kick a given user. Use this wisely""",
            '!Games' : "Splitgate, Dota 2, Valorant",
            '!Roll' : "@x rolled i-j: #",
            '!Kick' : "Hey everyone! @x just tried to kick @y! That bastard!"
}
        return commands.get(self.message, "Invalid command. All commands start with a capital letter.")