from state import *
from search import *


class Problem:
    def __init__(self):
        width = 10
        height = 5
        hospitals = [(4, 4), (9, 1)]
        houses = [(1, 1), (2, 3), (6, 0), (8, 4)]
        self.initial_state = State(width, height, hospitals, houses)


if __name__ == '__main__':
    problem = Problem()
    hill_climbing(problem)


