import math
import numpy as _np
import pygame.font
from tsp_file_reader import CitiesFromTSPFile

# Program constants
CITIES = CitiesFromTSPFile("tspData/berlin52.tsp")

# Algorithm constants
A = 1  # values high amounts of pheromones on paths
B = 6  # values shorter paths
P = 0.6  # pheromone evaporation constant
W = 0.2  # wandering, chance that ant will pick a random city

# setting the number of ants to the number of cities is most reliable
NUM_ANTS = CITIES.get_city_count()

# pygame things
MAX_FPS = 60
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1100, 800

# for visual
CITY_COLOR = (180, 180, 180)
ROUTE_COLOR = (90, 160, 100)
ROUTE_WIDTH = 2
CITY_RADIUS = 5
BORDER_PUFFER = 100
GRID_SQUARE_SIZE = 0.5
FONT_SIZE = 20
FONT = pygame.font.get_default_font()
TEXT_COLOR = (230, 230, 230)
MAX_NUMBER_OF_INFO_TEXTS = 15

# distances have to be calculated
DISTANCES = _np.ones(shape=(CITIES.get_city_count(), CITIES.get_city_count()))
for i, city in enumerate(CITIES):
    for j, other_city in enumerate(CITIES):
        dist = math.dist(city, other_city)
        DISTANCES[i][j] = dist
