from search import *
from state import *


def test_neighbors():
    problem = Problem.example()
    state_1 = problem.initial_state
    state_2 = state_1.clone()
    state_3 = state_1.clone()

    state_2.hospitals[0] = state_2.hospitals[0][0] - 2, state_2.hospitals[0][1] - 4
    state_3.hospitals[1] = state_2.hospitals[1][0] - 5, state_2.hospitals[1][1] + 1

    print(state_1)
    print(state_2)
    print(state_3)


if __name__ == '__main__':
    test_neighbors()