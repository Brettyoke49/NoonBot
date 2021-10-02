import random

class Roll:
    @staticmethod
    def roll(input: [], userMention):
        arguments = len(input)

        if arguments == 1:
            return userMention + "rolled from 1 to 100: " + str(random.randint(1, 100))
        elif arguments == 3:
            low = input[1]
            high = input[2]
            roll = 0

            try:
                roll = random.randint(int(low), int(high))
                return userMention + "rolled from " + low + " to " + high + ": " + str(roll)
            except:
                return "Invalid low/high values"

        else:
            return "Invalid number of arguments"