class EqualDiff:
    def __init__(self):
        self.value = 0
        self.max = 20

    def __next__(self):
        print("excute __next__ function")
        self.value += 1
        if self.value > self.max:
            raise StopIteration
        return self.value

    def __iter__(self):
        print("excute __iter__ function")
        return self

if __name__ == "__main__":
    ti = EqualDiff()
    #print("point 1")
    #l1 = list(ti)
    #print("point 2")
    #print(l1)

    for t in ti:
        print("one step")
        print(t)
