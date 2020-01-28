"""class MuffedCalculator:
    muffed = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffed:
                print("Division by zero is illegal")
            else:
                raise

    def makeCalc(self):
        try:
            a = int(input("Please input a number:"))
            b = int(input("Please input a number:"))
            self.result = a/b
            print(self.result)
        except ValueError:
            if self.muffed:
                print("string turn into int is illegal")
            else:
                raise

        except ZeroDivisionError:
            if self.muffed:
                print("Division by zero is illegal")
            else:
                raise

        except TypeError:
            if self.muffed:
                print("Division by not digital is illegal")
            else:
                raise
"""
class MuffedCalculator:
    muffed = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffed:
                print("Division by zero is illegal")
            else:
                raise

    def makeCalc(self):
        try:
            a = int(input("Please input a number:"))
            b = int(input("Please input a number:"))
            self.result = a/b
            print(self.result)
        except (ValueError, ZeroDivisionError, TypeError) as e:
            if self.muffed:
                print("illegal")
                print(e)
            else:
                raise

if __name__ == "__main__":
    #c = MuffedCalculator()
    #c.calc("34/0")
    
    #c = MuffedCalculator()
    #c.muffed = True
    #c.calc("34/0")

    c = MuffedCalculator()
    c.muffed = True
    c.makeCalc()
    pass
