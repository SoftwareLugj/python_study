class Rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height

    size = property(fget = getSize, fset = setSize)


if __name__ == "__main__":
    #o1 = Rectangle()
    #o1.setSize((150,100))
    #print(o1.width)
    #print(o1.height)

    o1 = Rectangle()
    o1.size = 150,100
    
    print(o1.width)
    print(o1.height)