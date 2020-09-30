from state import *
from random import choice


def hill_climbing(problem, random_restart=False):
    current_state = problem.initial_state
    if random_restart:
        current_state.random_start()
    while True:
        next_state = min(current_state.neighbors)
        if next_state >= current_state:
            return current_state
        current_state = next_state


def simulated_annealing(problem, schedule):
    current_state = problem.initial_state
    for t in range(1001):
        T = schedule(t)
        if T <= 0:
            return current_state

        neighbor_state = min(current_state.neighbors)

        ΔE = neighbor_state - current_state
        if ΔE > 0:
            current_state = neighbor_state
        else:
            # look at all the neighbors and pick one based on T and ΔE
            current_state = choice(current_state.neighbors)