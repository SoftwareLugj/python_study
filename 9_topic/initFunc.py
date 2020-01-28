class A:
    def __init__(self):
        self.name = "lugj"

    def __del__(self):
        print("delete " + self.name)

if __name__ == "__main__":
    o1 = A()
    print(o1.name)
    del o1
