import numpy as np
import pygame

from ant import Ant
from constants import NUM_CITIES, NUM_ANTS, MAX_FPS
from visualizer import ShortestRouteVisualizer


def main():
    pheromones = np.ones(shape=(NUM_CITIES, NUM_CITIES))

    # create some ants
    ants = []
    for i in range(NUM_ANTS):
        ants.append(Ant())

    # create variables for main loop
    visualizer = ShortestRouteVisualizer()
    clock = pygame.time.Clock()
    run = True
    while run:

        clock.tick(MAX_FPS)  # just so that it doesn't crash

        for event in pygame.event.get():
            # close window
            if event.type == pygame.QUIT:
                run = False

        # calculate ant routes
        routes = []
        for ant in ants:
            routes.append(ant.calculate_route(pheromones))

        # update pheromones here

        # display
        visualizer.visualize(routes)
        # make some text here that says calculating because we will be calculating the next routes
        #   before the next display occurs
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    main()
