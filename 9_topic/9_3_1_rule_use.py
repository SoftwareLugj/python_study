class ArithmeticSequence:
    def checkKey(self, key):
        if not isinstance(key, int):
            raise TypeError
        if key < 0:
            raise IndexError
            
    def __init__(self, start = 0, step = 1):
        self.start = start
        self.step = step
        self.changed = {}
    
    def __getitem__(self, key):
        """
        Get an item from the arithmetic sequence
        """
        self.checkKey(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        """
        modify an item which from the arithmetic sequence
        """
        self.checkKey(key)
        self.changed[key] = value

if __name__ == "__main__":
    o1 = ArithmeticSequence()
    print(o1[9])
    o1[9] = 100
    print(o1[9])
    #del o1[9]
    