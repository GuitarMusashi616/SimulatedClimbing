from state import *
from search import *


def hill_climbing_demo():
    # problem = Problem.generate(width=30, height=20, houses=8, hospitals=4)
    problem = Problem.example()
    print(problem)
    print(hill_climbing(problem))


def random_restart_demo():
    problem = Problem.generate(width=30, height=20, houses=8, hospitals=4)
    # problem = Problem.example()
    print(problem)
    print(hill_climbing(problem))
    print(hill_climbing(problem, True))
    print(hill_climbing(problem, True))
    print(hill_climbing(problem, True))


def schedule(t):
    return 10000 - t*10


def simulated_annealing_demo():
    problem = Problem.generate(width=30, height=20, houses=8, hospitals=4)
    # problem = Problem.example()
    print(problem)
    print(simulated_annealing(problem, schedule))


if __name__ == '__main__':
    hill_climbing_demo()



