import random

class Insect:
    def __init__(self):
        self.wings = 2

        self.legs = 4

        self.fly = range(1,10)

    def flight(self):    
        self.fly = random.randint(1,10)


    def get_flight(self):
        return self.fly
        


