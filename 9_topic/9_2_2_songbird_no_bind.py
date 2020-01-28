import bird

class SongBird(bird.Bird):
    def __init__(self):
        bird.Bird.__init__(self)
        self.sound = "ABCDEFG...XYZ"

    def sing(self):
        if not self.hanger:
            print(self.sound)
            self.hanger = True
        else:
            print("Too hanger to sing the song")

if __name__ == "__main__":
    b1 = SongBird()
    b1.sing()
    b1.eat()
    b1.sing()
    b1.eat()
    b1.fly()