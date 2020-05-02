"""This module contains the class responsible for defining rectangles."""


import pygame


class Rectangle:
    """Class to represent a rectangle."""

    def __init__(self, color, dimensions):
        self.color = color
        self.left, self.top, self.width, self.height = dimensions

    def draw(self, surface):
        """Draw the rectangle on the given surface."""
        pass

    def undraw(self):
        """Undraw the rectangle."""
        pass

    def change_color(self, color):
        """Change the rectangle's color."""
        pass

    def move(self, x, y):
        """Move the rectangle 'x' pixels to the right and 'y' pixels up. Returns a new
        rectangle instance.
        """
        pass

    def copy(self):
        """Return a copy of the current rectangle."""
        pass

