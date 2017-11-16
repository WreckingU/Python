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

class PokerApp(object):
    def __init__(self):
        self.dice = Dice()
        self.money = 100
    def wantToPlay(self):
        ans = raw_input("Do you wish to try your luck?")
        if ans[0].lower() == "y":
            return True
        else:
            return False
    def run(self):
        print "You currently have $100"
        while self.money >=10 and self.wantToPlay() == True:
            self.playRound()            
    def playRound(self):
        self.money -= 10
        self.doRolls()
        print self.dice.score()[0] + ". You Win! $" +  str(self.dice.score()[1])
        self.money += self.dice.score()[1]
        print "You currently have $" + str(self.money)
    def doRolls(self):
        self.dice.roll([0,1,2,3,4])
        rollNumber = 1
        print "Dice:", self.dice.dice
        toRoll = input("Enter list of which to change ([] to stop) ")
        while rollNumber < 2 and toRoll !=[]:
            self.dice.roll(toRoll)
            rollNumber += 1
            print "Dice:", self.dice.dice
            toRoll = input("Enter list of which to change ([] to stop) ")
            print "Dice:", self.dice.dice
        if toRoll == []:
            pass
            

game = PokerApp()
game.run()
