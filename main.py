from state import *
from search import *
from math import pow


def hill_climbing_demo():
    print("Hill Climbing Initial Board")
    # problem = Problem.generate(width=30, height=20, houses=8, hospitals=4)
    problem = Problem.example()
    print(problem)
    print(hill_climbing(problem))
    print('\n')


def random_restart_demo(problem):
    print("Random Restart Initial Board")
    print(problem)

    solutions = [hill_climbing(problem, True) for _ in range(4)]
    for solution, configurations in solutions:
        print(f"Configurations Evaluated: {configurations}")
        print(solution)
    print('\n')


def schedule(t):
    """Schedule function used by simulated annealing to get decrease in temperature"""
    return 2 * pow(.9, t//100)


def simulated_annealing_demo(problem):
    print("Simulated Annealing Initial Board")
    print(problem)

    solutions = [simulated_annealing(problem, schedule, True) for _ in range(4)]
    for solution, configurations in solutions:
        print(f"Configurations Evaluated: {configurations}")
        print(solution)
    print('\n')


def prompt_integer(string):
    number = None
    while not number:
        inp = input(string)
        try:
            number = int(inp)
        except ValueError:
            print("Please input an integer")
    return number


if __name__ == '__main__':
    print("Hill Climbing and Simulated Annealing Demo\n")
    width = prompt_integer("Enter an integer for the grid width: ")
    height = prompt_integer("Enter an integer for the grid height: ")
    houses = prompt_integer("Enter an integer for the number of houses: ")
    hospitals = prompt_integer("Enter an integer for the number of hospitals: ")
    print()

    grids = [Problem.generate(width=width, height=height, houses=houses, hospitals=hospitals) for _ in range(4)]

    for grid in grids:
        random_restart_demo(grid)
        simulated_annealing_demo(grid)



