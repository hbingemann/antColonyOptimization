# contains a list of cities that defines a route
import math
from constants import CITIES


class Route:

    def __init__(self, cities=None):
        self.cities = cities  # list of cities
        if self.cities is None:
            self.reset()  # reset the route if nothing was added

    def get_length(self):
        assert self.has_completed_route(), "Can't get the length of an incomplete route"
        length = 0
        for path in self.loop_through_paths():
            length += math.dist(*path)
        return length

    def add(self, city):
        assert not self.has_completed_route(), f"Route is too long, cannot add the city {city}"
        self.cities.append(city)

    def reset(self):
        self.cities = [CITIES.get_first()]

    def get(self, index):
        return self.cities[index]

    def get_city_count(self):
        return len(self.cities)

    def has_visited_city(self, city):
        return city in self.cities

    def get_current_city(self):
        return self.get(-1)  # last item is current city

    def has_completed_route(self):
        return self.get_city_count() >= CITIES.get_city_count()

    def loop_through_paths(self):
        assert self.has_completed_route(), "Can't loop through the paths of an incomplete route"
        for i in range(self.get_city_count()):
            yield self.get(i - 1), self.get(i)
