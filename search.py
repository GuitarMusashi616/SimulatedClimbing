from state import *
from random import random
from math import exp
from typing import Callable


def hill_climbing(problem: Problem, random_restart: bool = False):
    """The Hill Climbing Algorithm: picks the neighboring state with the highest increase in value

    :param problem: The problem object that wraps the state representation of the grid
    :param random_restart: whether or not to shuffle the hospitals at the start
    :returns: a state object representing the solution as well as an integer representing the configurations evaluated
    """
    current_state = problem.initial_state.clone()
    configs_evaluated = 0
    if random_restart:
        current_state.random_start()
    while True:
        next_state = min(current_state.neighbors)
        if next_state >= current_state:
            return current_state, configs_evaluated
        current_state = next_state
        configs_evaluated += 1


def simulated_annealing(problem: Problem, schedule: Callable[[int], int], time_steps: int = 1000, random_restart: bool = False):
    """The Simulated Annealing Algorithm: picks the neighboring state based on its increase in value and the current temperature

    :param problem: The problem object that wraps the state representation of the grid
    :param schedule: A callable that returns the temperature T given a time value t
    :param time_steps: The number of time steps that simulated annealing should undergo
    :param random_restart: whether or not to shuffle the hospitals at the start
    :returns: a state object representing the solution as well as an integer representing the configurations evaluated
    """
    current_state = problem.initial_state.clone()
    configs_evaluated = 0
    if random_restart:
        current_state.random_start()

    for t in range(time_steps):
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
