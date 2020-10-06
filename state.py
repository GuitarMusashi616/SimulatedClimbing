# Austin Williams and Jack Carrol
# Frank Moore
# Artificial Intelligence
# 5 October 2020

from random import randint
from math import inf
from typing import Tuple, Iterable


def manhattan_distance(coord_1: Tuple[int, int], coord_2: Tuple[int, int]):
    """Returns the vertical difference + the horizontal difference of the coordinates

    :param coord_1: A coordinate representing a point on a grid
    :param coord_2: Another coordinate representing a point on a grid
    """
    assert type(coord_1) == tuple and type(coord_2) == tuple
    assert len(coord_1) == 2 and len(coord_2) == 2

    return abs(coord_1[0] - coord_2[0]) + abs(coord_1[1] - coord_2[1])


def generate_unique_coords(num_new: int, existing_coords: Iterable[Tuple[int, int]] = [], width: int = 10,
                           height: int = 5):
    """Creates a unique set of coordinates of length num_new that are also not the same as any coords in existing_coords

    :param num_new: specifies how many new random unique coordinates are needed
    :param existing_coords: an iterable of coordinates, new coordinates will not be the same as any coordinates in this iterable
    :param width: specifies the width of the grid
    :param height specifies the height of the grid
    """
    new_coords = {}
    while len(new_coords) < num_new:
        new_coord = (randint(0, width - 1), randint(0, height - 1))
        if new_coord not in existing_coords:
            new_coords[new_coord] = True
    return list(new_coords)


class State:
    """Used to store, manipulate, and view the contents of each of the states"""

    def __init__(self, width, height, houses, hospitals):
        """Used to initialize the state object

        :param width: specifies the width of the grid
        :param height specifies the height of the grid
        :param houses: specifies the number of houses in the grid
        :param hospitals specifies the number of hospitals im the grid
        """
        self.width = width
        self.height = height
        self.houses = houses
        self.hospitals = hospitals

    def __repr__(self):
        """Returns a representation of the state, H's represent hospitals, O's represent houses"""
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
        """Returns the total cost of the state configuration"""
        return self.get_value()

    def get_value(self):
        """Returns the total cost of the state configuration"""
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
        """Returns the up to 8 neighboring states that correspond to the hospitals moving up, down, left, or right"""
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
        """Returns a copy of the state"""
        return State(self.width, self.height, self.houses.copy(), self.hospitals.copy())

    def is_accessible(self, coord: Tuple[int, int]):
        """Returns True if the coordinate is within the grid bounds and there are no overlapping hospitals or houses
        for the coordinate

        :param coord: The coordinate of either a hospital or house
        """
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
        """Shuffle the hospital locations"""
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


class Problem:
    """A class that is used to generate problems, each problem has a state and can be used by a search algorithm"""

    def __init__(self, state: State):
        """Used to initialize a problem

        :param state: used to store in the Problem object
        """
        self.initial_state = state

    def __repr__(self):
        """Used to return a string representation of the current state of the grid"""
        return repr(self.initial_state)

    @classmethod
    def generate(cls, width: int, height: int, houses: int, hospitals: int = 2):
        """Creates a Problem object using the width, height, houses, and hospitals arguments

        :param width: The width of the grid
        :param height: The height of the grid
        :param houses: The number of houses in the grid
        :param hospitals: The number of hospitals in the grid
        """
        coords = generate_unique_coords(houses + hospitals, [], width, height)
        return Problem(State(width, height, coords[:houses], coords[houses:]))

    @classmethod
    def example(cls):
        """Returns an example problem with the values below (matches the one from the assignment description)"""
        width = 10
        height = 5
        hospitals = [(4, 4), (9, 1)]
        houses = [(1, 1), (2, 3), (6, 0), (8, 4)]
        return Problem(State(width, height, houses, hospitals))
