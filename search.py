from state import *
from random import random
from math import exp


def hill_climbing(problem, random_restart=False):
    current_state = problem.initial_state
    configs_evaluated = 0
    if random_restart:
        current_state.random_start()
    while True:
        next_state = min(current_state.neighbors)
        if next_state >= current_state:
            return current_state, configs_evaluated
        current_state = next_state
        configs_evaluated += 1


def simulated_annealing(problem, schedule, random_restart=False):
    current_state = problem.initial_state
    configs_evaluated = 0
    if random_restart:
        current_state.random_start()

    for t in range(1000):
        T = schedule(t)
        if T <= 0:
            return current_state

        neighbor_state = min(current_state.neighbors)

        ΔE = neighbor_state - current_state
        if ΔE > 0:
            current_state = neighbor_state
            configs_evaluated += 1
        else:
            # look at all the neighbors and pick one based on T and ΔE
            prob = exp(ΔE/T)
            rand = random()
            if prob >= rand:
                current_state = neighbor_state
                configs_evaluated += 1
    return current_state, configs_evaluated
