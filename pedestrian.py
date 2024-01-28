from random import randint
'''
possible directions: 
    12
    23
    34
    41
    24
    13
    reverses are also options
'''
#each crosswalk will have 120 steps

class Pedestrian: 
    def __init__(self): 
        temp = randint(1, 4)
        temp2 = randint(1, 4)
        self.start = temp
        self.end = temp2
        self.rulebreaker = randint(0, 1)
        self.velocity = randint(1, 20) 
        self.moving = False
        self.currentPosition = 0

    def update(self): 
        self.currentPosition += 1



