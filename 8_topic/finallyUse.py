if __name__ == "__main__":
    try:
        a = 1/0
    except NameError:
        print("division by zero")
    else:
        print("no exception occupation")
    finally:
        print("finally")