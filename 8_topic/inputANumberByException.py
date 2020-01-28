if __name__ == "__main__":
    while(True):
        try:
            a = int(input("Please input a number:"))
            b = int(input("Please input a number:"))
            print(a/b)
        except (ZeroDivisionError, TypeError):
            print("Please input valid type or correct expression")
        else:
            break;
