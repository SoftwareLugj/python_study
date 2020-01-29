def sc(lx):
    for x in lx:
        print("excute sc function , current x = " + str(x))
        yield x

if __name__ == "__main__":
    x = [x for x in range(10) if x%2 == 0]
    for a in sc(x):
        print("point 1")
        print(a)