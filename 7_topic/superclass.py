import defineClass

class C(defineClass.A):
    pass
    def add(self):
        pass

class D(defineClass.A, defineClass.B):
    pass

if __name__ == "__main__":
    #o1 = C();
    #print(issubclass(C, defineClass.A))

    o2 = D();
    print(issubclass(D, defineClass.A))
    print(issubclass(D, defineClass.B))
    print(D.__bases__)
    print(isinstance(o2, D))
    print(o2.__class__)
    print(type(o2))
    #print(o2.__bases__)
    pass
