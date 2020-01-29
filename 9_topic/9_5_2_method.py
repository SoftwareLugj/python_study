from m9_5_1_property_func import Rectangle

class NRectangle(Rectangle):
    @staticmethod
    def smeth():
        print("This is a static method")

    @classmethod
    def cmeth(cls):
        print("This is a class method of " + str(cls))

if __name__ == "__main__":
    o1 = NRectangle()
    o1.smeth()
    o1.cmeth()
    NRectangle.smeth()
    NRectangle.cmeth()
    pass