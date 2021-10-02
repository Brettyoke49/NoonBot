import random

class Roll:
    userMention = ""

    def __init__(self, userMention):
        self.userMention = userMention
        pass

    def roll(self, low = None, high = None):
        if low == None and high == None:
            return self.userMention + "rolled from 1 to 100: " + str(random.randint(1, 100))
        elif low != None and high != None:
            try:
                roll = random.randint(low, high)
                return self.userMention + "rolled from " + str(low) + " to " + str(high) + ": " + str(roll)
            except:
                return "Invalid low/high values"
        else:
            return None