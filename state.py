from random import randint
from math import inf


def manhattan_distance(coord_1, coord_2):
    assert type(coord_1) == tuple and type(coord_2) == tuple
    assert len(coord_1) == 2 and len(coord_2) == 2

    return abs(coord_1[0] - coord_2[0]) + abs(coord_1[1] - coord_2[1])


def generate_unique_coords(num_new, existing_coords=[], width=10, height=5):
    new_coords = {}
    while len(new_coords) < num_new:
        new_coord = (randint(0,width-1), randint(0, height-1))
        if new_coord not in existing_coords:
            new_coords[new_coord] = True
    return list(new_coords)


class Problem:
    def __init__(self, state):
        self.initial_state = state

    def __repr__(self):
        return repr(self.initial_state)

    @classmethod
    def generate(cls, width, height, houses, hospitals):
        coords = generate_unique_coords(houses+hospitals, [], width, height)
        return Problem(State(width, height, coords[:houses], coords[houses:]))

    @classmethod
    def example(cls):
        width = 10
        height = 5
        hospitals = [(4, 4), (9, 1)]
        houses = [(1, 1), (2, 3), (6, 0), (8, 4)]
        return Problem(State(width, height, houses, hospitals))

    def shuffle_hospitals(self):
        self.initial_state.random_start()


class State:
    def __init__(self, width, height, houses, hospitals):
        self.width = width
        self.height = height
        self.houses = houses
        self.hospitals = hospitals

    def __repr__(self):
        string = f"Cost: {self.value}\n"
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.hospitals:
                    string += "H"
                elif (x, y) in self.houses:
                    string += "O"
                else:
                    string += "-"
            string += '\n'
        return string

    @property
    def value(self):
        return self.get_value()

    def get_value(self):
        # takes O(houses*hospitals) time
        hospital_distances = []
        for house in self.houses:
            lowest = inf
            for hospital in self.hospitals:
                value = manhattan_distance(house, hospital)
                if value < lowest:
                    lowest = value
            hospital_distances.append(lowest)
        return sum(hospital_distances)

    @property
    def neighbors(self):
        neighbors = []
        for i, hospital in enumerate(self.hospitals):
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                coord = (hospital[0] + dx, hospital[1] + dy)
                if self.is_accessible(coord):
                    new_state = self.clone()
                    new_state.hospitals[i] = coord
                    neighbors.append(new_state)
        return neighbors

    def clone(self):
        return State(self.width, self.height, self.houses.copy(), self.hospitals.copy())

    def is_accessible(self, coord):
        assert type(coord) == tuple
        assert len(coord) == 2

        if 0 <= coord[0] < self.width and 0 <= coord[1] < self.height:
            pass
        else:
            return False

        if coord in self.hospitals or coord in self.houses:
            return False

        return True

    def random_start(self):
        """shuffle the hospital locations"""
        # add house coords to dic
        # create num_hospitals more numbers
        # return the new numbers
        self.hospitals = generate_unique_coords(len(self.hospitals), self.houses, self.width, self.height)

    def __lt__(self, other):
        assert type(self) == State
        assert type(other) == State
        return self.value < other.value

    def __ge__(self, other):
        assert type(self) == State
        assert type(other) == State
        return self.value >= other.value

    def __sub__(self, other):
        assert type(self) == State
        assert type(other) == State
        return self.value - other.value
