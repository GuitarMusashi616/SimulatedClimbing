from state import *


def hill_climbing(problem):
    current_state = problem.initial_state
    while True:
        next_state = current_state.highest_valued_neighbor()
        if next_state <= current_state:
            return current_state
        current_state = next_state


def simulated_annealing(problem, schedule):
    current_state = problem.initial_state
    for t in range(1000):
        T = schedule(t)
        if not T:
            return current_state

        neighbor_state = current_state.highest_valued_neighbor()

        ΔE = neighbor_state - current_state
        if ΔE > 0:
            current_state = neighbor_state
        else:
            # look at all the neighbors and pick one based on T and ΔE
            current_state = max(current_state.neighbors)
