# Austin Williams and Jack Carrol
# Frank Moore
# Artificial Intelligence
# 5 October 2020

from state import *
from search import *
from math import pow


def hill_climbing_demo():
    """Demonstrates the Hill Climbing example from the assignment description"""
    print("Hill Climbing Initial Board")
    # problem = Problem.generate(width=30, height=20, houses=8, hospitals=4)
    problem = Problem.example()
    print(problem)
    print(hill_climbing(problem))
    print('\n')


def random_restart_demo(problem: Problem):
    """Runs the Hill Climbing with Random Restart algorithm 4 times for the given problem/ grid

    :param problem: The problem object that wraps the state representation of the grid
    """
    print("Random Restart Initial Board")
    print(problem)

    solutions = [hill_climbing(problem, True) for _ in range(4)]
    for solution, configurations in solutions:
        print(f"Configurations Evaluated: {configurations}")
        print(solution)
    print('\n')


def schedule(t: int) -> int:
    """Schedule function used by simulated annealing to get decrease in temperature

    :param t: the time value as an integer
    :returns: a temperature T
    """
    return 2 * pow(.9, t//100)


def simulated_annealing_demo(problem: Problem, time_steps: int):
    """Runs the Simulated Annealing Algorithm 4 times for the given problem/ grid

    :param problem: The problem object that wraps the state representation of the grid
    :param time_steps: The number of time steps that simulated annealing should undergo
    """
    print("Simulated Annealing Initial Board")
    print(problem)

    solutions = [simulated_annealing(problem, schedule, time_steps, True) for _ in range(4)]
    for solution, configurations in solutions:
        print(f"Configurations Evaluated: {configurations}")
        print(solution)
    print('\n')


def prompt_integer(string: str) -> int:
    """Continually prompts the user until an integer is received

    :param string: text that should be displayed by the prompt
    """
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
        simulated_annealing_demo(grid, 1000)



