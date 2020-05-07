"""This module contains views for the sorting visualizer GUI."""


import pygame


class SortingVisualizerGUI:
    """Class to represent the main GUI view for the visualizer."""

    def __init__(
        self,
        navbar,
        buttons,
        bars,
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
        self.navbar = navbar
        self.navbar.draw()
        self.buttons = buttons
        self.bars = bars
        for button in self.buttons:
            button.draw()
        for bar in self.bars:
            bar.draw()
        pygame.display.flip()

    def get_clicked_element(self):
        """Return the element on the screen that was clicked by the user."""
        pass

    def update(self, element):
        """Redraw the given element on the screen."""
        pass

    def display_message(self, message, coordinates):
        """Display the given message on the screen."""
        pass

    def swap(self, bar_one, bar_two):
        """Swap both of the given bars' positions."""
        #both bars will be red when this method is called.
        #first, swap them
        #next, turn them green to indicate they've been swapped
        pass

    def sorting_finish(self):
        """Change the colors of all of the bars to indicate
        that they are sorted.
        """
        #change them to green first and then to purple
        pass

    def quit(self):
        """Return True if the user has closed the pygame window."""
        for event in pygame.event.get(eventtype=pygame.QUIT):
            if event is not None:
                return True
        return False