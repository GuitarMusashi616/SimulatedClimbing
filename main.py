




def hill_climbing(problem):
    current = problem.initial_state
    while True:
        neighbor = current.highest_valued_neighbor()
        if neighbor.value <= current.value:
            return current.state
        current = neighbor

def simulated_annealing(problem, schedule):
    current = Node(problem.initial_state)
    for t in range(1000):
        T = schedule(t)
        if not T:
            return current

        neighbor = current.highest_valued_neighbor()

        delta_E = neighbor.value - current.value
        if delta_E > 0:
            current = next
        else:
            current = next if prob(delta_E, T)



if __name__ == '__main__':
    pass