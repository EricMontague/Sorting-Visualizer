"""This module contains views for the sorting visualizer GUI."""


import pygame
import sys
from visualizer.widget_types import WidgetType


class SortingVisualizerGUI:
    """Class to represent the main GUI view for the visualizer."""

    def __init__(self, screen, navbar, buttons, bars):
        self.screen = screen
        self.navbar = navbar
        self.buttons = buttons
        self.bars = bars
        self.navbar.draw(self.screen)
        for button in self.buttons:
            button.draw(self.screen)
        for bar in self.bars:
            bar.draw(self.screen)
        pygame.display.flip()

    def get_clicked_element(self):
        """Return the element on the screen that was clicked by the user."""
        elements = self.navbar.elements + self.buttons
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    for element in elements:
                        if element.clicked(position):
                            return element, position

    def update(self, element):
        """Redraw the given element on the screen."""
        pass

    def display_message(self, message, coordinates):
        """Display the given message on the screen."""
        pass

    def swap(self, bar_one, bar_two):
        """Swap both of the given bars' positions."""
        # both bars will be red when this method is called.
        # first, swap them
        # next, turn them green to indicate they've been swapped
        pass

    def sorting_finish(self):
        """Change the colors of all of the bars to indicate
        that they are sorted.
        """
        # change them to green first and then to purple
        pass

    def reset(self):
        """Reset the GUI to its original state."""
        pass

