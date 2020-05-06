"""This module contains classes that represent bars in the GUI window."""


import pygame


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
class NavBar:
    """Class to represent a navigation bar for the GUI."""

    def __init__(self, surface, rectangle, elements):
        self.rectangle = rectangle
        self.rectangle.draw(surface)
        self.elements = elements
        self.draw()

    def draw(self):
        """Draw the navigation bar onto the screen."""
        for element in self.elements:
            element.draw(self._get_surface())

    def click(self, position):
        """Alter the state of the element in the navbar that
        was clicked.
        """
        for element in self.elements:
            if element.type == "LABEL":
                if element.clicked(position):
                    element.change_color("ENTER COLOR HERE")
            elif element.type == "BUTTON":
                if element.clicked_increase(position):
                    element.increment()
                else:
                    element.decrement()

    def _get_surface(self):
        """Return the rectangular area of the navbar's area as
        a pygame Surface object."""
        return pygame.Surface(self.rectangle.width, self.rectangle.height)
        

class Bar:
    """Class to represent a bar in the GUI. The bar in turns
    represents a number in a list.
    """

    def __init__(self, surface, label, rectangle):
        self.rectangle = rectangle
        self.rectangle.draw(surface)
        self.label = label
        self.label.draw(surface)

    def draw(self):
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


