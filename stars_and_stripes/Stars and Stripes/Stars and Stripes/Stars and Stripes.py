def printTwentyStars():
    print "*" * 20

def printTwentyDashes():
    print "-" * 20

def printSmile():
    print ":)" * 200


def printCOM():
    print "~" * 240
    
def printArrows():
    print "<---->" * 240

def printK():
    print "<^>" * 240
    TwoBlankLines()
    print " : " * 240

def TwoBlankLines():
    print "" * 20
    print "" * 20

def printASmallBox():
    printTwentyDashes()
    printTwentyStars()
    printTwentyDashes()
    printTwentyStars()
    printTwentyDashes()
    printTwentyStars()
    printTwentyDashes()


def printABigBox():
    printASmallBox()
    printASmallBox()

def printAwesomeBox():
    printSmile()
    TwoBlankLines()
    printCOM()
    TwoBlankLines()
    printArrows()
    TwoBlankLines()
    printK()
    


printASmallBox()
TwoBlankLines()
printABigBox()
TwoBlankLines()
printAwesomeBox()




