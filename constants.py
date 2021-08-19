import math
import numpy as _np
import pygame.font


# Algorithm constants
A = 1  # values high amounts of pheromones on paths
B = 5  # values shorter paths
P = 0.6  # pheromone evaporation constant
W = 0.1  # wandering, chance that ant will pick a random city

# Program constants
CITIES = list({
    (1, 3), (4, 4), (3, 2),
    (4, 5), (7, 4), (1, 1),
    (8, 5), (2, 2), (5, 5),
    (6, 6), (9, 2), (5, 7),
    (9, 9), (2, 7), (3, 5)})
NUM_CITIES = len(CITIES)

# setting the number of ants to the number of cities is most reliable
NUM_ANTS = NUM_CITIES

# pygame things
MAX_FPS = 60
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1100, 800

# for visual
CITY_COLOR = (180, 180, 180)
ROUTE_COLOR = (90, 160, 100)
ROUTE_WIDTH = 2
CITY_RADIUS = 10
BORDER_PUFFER = 100
GRID_SQUARE_SIZE = 50
FONT_SIZE = 20
FONT = pygame.font.get_default_font()
TEXT_COLOR = (230, 230, 230)

# calculate the distances constant
DISTANCES = _np.ones(shape=(NUM_CITIES, NUM_CITIES))
for i, city in enumerate(CITIES):
    for j, other_city in enumerate(CITIES):
        dist = math.dist(city, other_city)
        DISTANCES[i][j] = dist
