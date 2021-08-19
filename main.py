import numpy as np
import pygame

from ant import Ant
from constants import DISTANCES, NUM_ANTS, MAX_FPS, P
from visualizer import ShortestRouteVisualizer


def main():
    pheromones = np.ones(shape=DISTANCES.shape)
    iterations = 0

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
        pheromone_drops = []
        for ant in ants:
            route, dropped_pheromones = ant.travel(pheromones)
            routes.append(route)
            pheromone_drops.append(dropped_pheromones)

        # pheromone evaporation
        pheromones *= np.full(shape=pheromones.shape, fill_value=1-P)

        # add pheromones that the ants dropped
        for dropped_pheromones in pheromone_drops:
            pheromones += dropped_pheromones

        # increase iterations
        iterations += 1

        # display
        visualizer.visualize(routes, iterations)
        # make some text here that says calculating because we will be calculating the next routes
        #   before the next display occurs
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    main()
