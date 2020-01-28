class A:
    def talk(self):
        print("I'm A")

class B(A):
    pass

if __name__ == "__main__":
    o1 = B()
    o1.talk()