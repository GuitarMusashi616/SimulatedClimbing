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


def random_restart_demo():
    print("Random Restart Initial Board")
    problem = Problem.generate(width=30, height=20, houses=8, hospitals=2)
    print(problem)

    solutions = [hill_climbing(problem, True) for _ in range(4)]
    for solution, configurations in solutions:
        print(f"Configurations Evaluated: {configurations}")
        print(solution)
    print('\n')


def schedule(t):
    return 2 * pow(.9, t//100)


def simulated_annealing_demo():
    print("Simulated Annealing Initial Board")
    problem = Problem.generate(width=30, height=20, houses=8, hospitals=2)
    print(problem)

    solutions = [simulated_annealing(problem, schedule, True) for _ in range(4)]
    for solution, configurations in solutions:
        print(f"Configurations Evaluated: {configurations}")
        print(solution)
    print('\n')


if __name__ == '__main__':
    random_restart_demo()
    simulated_annealing_demo()



