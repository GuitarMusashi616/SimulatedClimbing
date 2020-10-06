from search import *
from state import *
from random import randint


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


def test_more_unique_coords():
    random_existing = [(randint(0,9), randint(0,5)) for _ in range(20)]
    amount = 5

    lst = generate_unique_coords(amount, random_existing)
    len(lst) == amount

    for item in lst:
        assert item not in random_existing


if __name__ == '__main__':
    test_more_unique_coords()