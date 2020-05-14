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

    def __init__(self, dimensions, elements):
        self.rectangle = pygame.Rect(dimensions)
        self.elements = elements

    def draw(self, surface):
        """Draw the navigation bar onto the screen."""
        navbar_surface = self._get_surface()
        for element in self.elements:
            element.draw(navbar_surface)

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

    def __init__(self, label, dimensions):
        self.rectangle = pygame.Rect(dimensions)
        self.label = label

    def draw(self, surface):
        """Draw the bar on the screen."""
        bar_surface = self._get_surface()
        surface.blit(self.rectangle, bar_surface)
        label_center = ()
        self.label.draw(surface, label_center)

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
    def create_bars(surface, values):
        """Return NumberBar instances, each with one
        of the given values.
        """
        pass
    