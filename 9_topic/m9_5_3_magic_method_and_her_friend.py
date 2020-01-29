
from m9_5_1_property_func import Rectangle

class MRectangle(Rectangle):
    def __setattr__(self, name, value):
        if name == "size":
            self.width, self.height = value
        else:
            self.__dict__[name] = value

    """
    def __getattr__(self, name):
        if name == "size":
            return self.width, self.height
        else:
            self.__dict__[name] = None
            return self.__dict__[name]
    """

    def __getattribute__(self, name):
        if name == "size":
            return self.width, self.height
        try:return super(MRectangle, self).__getattribute__(name)
        except AttributeError:
            super(MRectangle, self).__dict__[name] = None
            return None

if __name__ == "__main__":
    o1 = MRectangle()
    #o1.s = 123
    print(o1.size)
    print(o1.s1)