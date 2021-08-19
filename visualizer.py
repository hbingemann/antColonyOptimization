import pygame
import numpy as np

from constants import *
from route import Route


# shows shortest route as it updates as ants travel
class ShortestRouteVisualizer:

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.shortest_route = Route(CITIES)  # default route is just whatever order the cities are in
        # initialize grid
        self.grid_width = np.amax(CITIES)
        self.grid_height = self.grid_width
        self.grid_dimensions = self.grid_width, self.grid_height
        # initialize fonts
        self.font = pygame.font.Font(FONT, FONT_SIZE)

    def visualize(self, routes, iterations):

        # check if there was a new shortest route
        for route in routes:
            if route.get_length() < self.shortest_route.get_length():
                self.shortest_route = route

        self.screen.fill((20, 20, 20))  # dark grey
        self._visualize_cities()
        self._visualize_shortest_route()
        # display the text
        self._display_texts(f"Path Length: {round(self.shortest_route.get_length(), 3)}",
                            f"Iteration: {iterations}")

    def _visualize_cities(self):
        # make a circle at each city location
        for city_coords in CITIES:
            city_x, city_y = ShortestRouteVisualizer.get_city_visual_coordinates(city_coords)
            pygame.draw.circle(self.screen, CITY_COLOR, (city_x, city_y), CITY_RADIUS)

    def _visualize_shortest_route(self):
        for path in self.shortest_route.loop_through_paths():
            city1, city2 = [ShortestRouteVisualizer.get_city_visual_coordinates(_city) for _city in path]
            pygame.draw.line(self.screen, ROUTE_COLOR, city1, city2, width=ROUTE_WIDTH)

    def _display_texts(self, *texts):
        assert len(texts) <= MAX_NUMBER_OF_INFO_TEXTS, "Tried to display too many texts"
        for text_number, text in enumerate(texts):
            text_surface = self.font.render(text, True, TEXT_COLOR)
            text_position = SCREEN_WIDTH - (text_surface.get_width() + 100), 50 + 50 * text_number
            self.screen.blit(text_surface, text_position)

    @staticmethod
    def get_city_visual_coordinates(city_graph_coords):
        return [city_dim * GRID_SQUARE_SIZE + BORDER_PUFFER for city_dim in city_graph_coords]
