import math

from route import Route
from constants import CITIES, A, B, W, DISTANCES
import numpy as np


class Ant:

    def __init__(self):
        pass

    def choose_next_city(self, route, pheromones):
        unvisited_cities = [city for city in CITIES if not route.has_visited_city(city)]
        # check wandering first
        if np.random.random_sample() < W:
            return unvisited_cities[np.random.randint(0, len(unvisited_cities))]
        current_city = route.get_current_city()
        # calculate the desirability of each path and the total desirability
        total_desirability = 0
        desirabilities = []
        for unvisited_city in unvisited_cities:
            # get the variables for the equation
            pheromones_on_path = pheromones[CITIES.get_index(current_city)][CITIES.get_index(unvisited_city)]
            path_shortness_value = 1 / DISTANCES[CITIES.get_index(current_city)][CITIES.get_index(unvisited_city)]
            # calculate desirability equation
            desirability = math.pow(pheromones_on_path, A) * math.pow(path_shortness_value, B)
            desirabilities.append(desirability)
            total_desirability += desirability
        # calculate what the probability (0 - 1) of going on each path is based off of their desirability
        probabilities = []
        for desirability in desirabilities:
            probability = desirability / total_desirability
            probabilities.append(probability)
        # now choose the next city based off of the probabilities
        choice = np.random.choice([i for i in range(len(unvisited_cities))], p=probabilities)
        return unvisited_cities[choice]

    def travel(self, pheromones):
        route = Route()
        dropped_pheromones = np.zeros(shape=pheromones.shape)
        going_on_route = True
        while going_on_route:
            route.add(self.choose_next_city(route, pheromones))
            if route.get_city_count() == CITIES.get_city_count():
                # visited every city
                going_on_route = False
        # calculate where pheromones are dropped
        for city1, city2 in route.loop_through_paths():
            city1_index, city2_index = CITIES.get_index(city1), CITIES.get_index(city2)
            dropped_pheromones[city1_index][city2_index] = \
                dropped_pheromones[city2_index][city1_index] = \
                1 / route.get_length()
        return route, dropped_pheromones
