from random import randint

class Dice(object):
    dice = []
    def __init__(self):
        for i in range(5):
            self.dice.append(randint(1,6))
    def roll(self, reroll):
        for i in reroll:
            self.dice[i] = randint (1,6)
    def score(self):
        counts = [0, 0, 0, 0, 0, 0, 0]
        for i in self.dice:
            counts[i] += 1

        if 5 in counts:
            return "Five of a Kind", 30
                             
        elif 4 in counts:
            return "Four of a Kind", 15
                             
        elif 3 in counts and 2 in counts:
            return "Full House", 12
                             
        elif 3 in counts:
            return "Three of a Kind", 8
                             
        elif counts.count(2) == 2:
            return "Two Pairs", 5
        elif not (2 in counts) and (counts[i] == 0 or counts[6] == 0):
            return "Straight", 20
        else:
            return "Garbage", 0


hand = Dice()
print hand.dice
hand.roll([0,2,3])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""

hand.roll([0,1,2,3,4])
print hand.dice                            
print hand.score()
print ""





