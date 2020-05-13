"""This module contains classes that represent bars in the GUI window."""


import pygame
from visualizer.labels import Label

# Right most side of navbar:
# "Selection Sort"
# "Insertion Sort"
# "Merge Sort"
# "Bubble Sort"
# "Heapsort"
# "Quicksort"


#To get a surface from a rectangle, you can create a new Surface
#object using the rectangle's dimensions
# e.g. surf = pygame.Surface((a.w, a.h))
class NavigationBar:
    """Class to represent a navigation bar for the GUI."""

    def __init__(self, rectangle, elements):
        self.rectangle = rectangle
        self.elements = elements

    def draw(self, surface):
        """Draw the navigation bar onto the screen."""
        for element in self.elements:
            element.draw(self._get_surface())

    def click(self, position):
        """Alter the state of the element in the navbar that
        was clicked.
        """
        pass

    def _get_surface(self):
        """Return the rectangular area of the navbar's area as
        a pygame Surface object."""
        return pygame.Surface(self.rectangle.width, self.rectangle.height)
        

class NumberBar:
    """Class to represent a bar in the GUI. The bar in turns
    represents a number in a list.
    """

    def __init__(self, label, rectangle):
        self.rectangle = rectangle
        self.label = label

    def draw(self, surface):
        """Draw the bar on the screen."""
        pass

    def flash(self, color):
        """Change the bar's color to the provided color and then back
        again.
        """
        pass

    def change_color(self, color):
        """Change the bar's color."""
        pass

    def _get_surface(self):
        """Return the rectangular area of the navbar's area as
        a pygame Surface object."""
        return pygame.Surface(self.rectangle.width, self.rectangle.height)



class NumberBarFactory:
    """Factory class to generate NumberBar instances."""

    @staticmethod
    def create_bars(values):
        """Return NumberBar instances, each with one
        of the given values.
        """
        pass
    