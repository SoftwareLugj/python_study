class Bird:
    __number = 0
    def __init__(self):
        Bird.__number = Bird.__number + 1
        self.hanger = True

    def getNumber(self):
        print("Currently, Bird have %d" % (Bird.__number))
        return Bird.__number

    def eat(self):
        if self.hanger:
            print("Ahhhh, I eat many food, thanks")
            self.hanger = False
        else:
            print("Emmm, I can't eat anything")

    def fly(self):
        if self.hanger:
            print("Too hanger to fly, Give me a lot food, Please")
        else:
            print("I will fly to a remote place, one times goes, I reciving here")
            self.hanger = True

if __name__ == "__main__":
    pass
    