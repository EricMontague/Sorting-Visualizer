"""This module contains views for the sorting visualizer GUI."""


import pygame


class SortingVisualizerGUI:
    """Class to represent the main GUI view for the visualizer."""

    def __init__(
        self,
        navigation_bar,
        width=1080,
        height=600,
        background_color=(255, 255, 255),
    ):
        # background color defaults to white
        pygame.init()
        self.window = pygame.display.set_mode(size=(width, height))
        self.window.fill(background_color)
        self.width = width
        self.height = height
        self.background_color = background_color
        self.navigation_bar = navigation_bar
        self.navigation_bar.draw()
        pygame.display.flip()

