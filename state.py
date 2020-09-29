from random import randint

class State:
    def __init__(self, width, height, hospitals, houses):
        self.width = width
        self.height = height
        self.hospitals = hospitals
        self.houses = houses

    @classmethod
    # generate 8 random (x,y) coordinates with no duplicates
    def generate(cls, width=10, height=5, houses=4, hospitals=2):
        hospital_a = (randint(0, width-1), randint(0, height-1))
        hospital_b = (randint(0, width-1), randint(0, height-1))
        while hospital_a == hospital_b:
            hospital_b = (randint(0, width), randint(0, height))

        return State(width, height, hospital_a, hospital_b)