class Kick:
    @staticmethod
    def kick(input: [], userMention):
        arguments = len(input)

        if arguments == 2:
            userToKick = input[1]
            if userToKick[0:3] != '<@!':
                return "Must specify a user"
            else:
                return "Hey everyone! " + userMention + " just tried to kick " + input[1] + "! What a bastard!"
        else:
            return "Invalid number of arguments"