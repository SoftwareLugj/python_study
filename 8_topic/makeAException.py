#import Exception

class MyException(Exception):
    pass

if __name__ == "__main__":
    #raise Exception("make a exception")
    #raise AttributeError
    raise MyException
    pass
