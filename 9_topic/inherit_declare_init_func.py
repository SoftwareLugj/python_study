import inherit_no_declare_init_func as inherit

class C(inherit.A):
    def talk(self):
        print("I'm C")

if __name__ == "__main__":
    o1 = C()
    o1.talk()