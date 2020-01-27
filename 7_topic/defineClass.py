class A:
    #print("我是class A")
    pass

class B:
    numbers = 0
    def add(self):
        numbers = numbers + 1


if "__main__" == __name__:
    #o1 = A()
    o2 = B()
    print(o2.numbers)
    print(B.numbers)
    print(B.numbers is o2.numbers)
    pass
