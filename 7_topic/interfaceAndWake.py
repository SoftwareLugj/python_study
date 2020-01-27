import superclass as spc

class A(spc.D):
    def add(self):
        pass

if __name__ == "__main__":
    #print(hasattr(A, "name"))
    
    #print(getattr(A, "name", None))
    #print(hasattr(A, "name"))

    #print(setattr.__doc__)
    #print(setattr(A, "name", "xiaoming"))
    #print(getattr(A, "name", None))
    #print(hasattr(A, "name"))

    print(A.add)
    print(A.add.__dict__)
    print(dir(A.add))
    print(A.__dict__)
    pass
