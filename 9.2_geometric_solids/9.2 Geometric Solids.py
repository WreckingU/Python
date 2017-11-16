class RectangularPrism(object):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        
    def volume(self):
        return (self.length * self.width * self.height)
    
    def surfaceArea(self):
        return ((self.length * self.width * 2) + (self.length * self.height * 2) + (self.width * self.height * 2)) 
    def __repr__(self):
        return "Rectanglular Prism with length %d width %d and height %d" % (self.length, self.width, self.height)

class Cube(RectangularPrism):
    def __init__(self, sideLength):
        self.length = sideLength
        self.width = sideLength
        self.height = sideLength
    def __repr__(self):
        return "Cube with a side %d" % (self.length)


box1 = RectangularPrism(2, 3, 4)
print box1
print "Volume = " + str(box1.volume())
print "Suface Area = " + str(box1.surfaceArea())

print

box2 = Cube(2)
print box2
print "Volume = " + str(box2.volume())
print "Suface Area = " + str(box2.surfaceArea())
