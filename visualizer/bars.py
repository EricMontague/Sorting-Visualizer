"""This module contains classes that represent bars in the GUI window."""


import pygame
from visualizer.labels import Label
from visualizer.widget_types import WidgetType

# Right most side of navbar:
# "Selection Sort"
# "Insertion Sort"
# "Merge Sort"
# "Bubble Sort"
# "Heapsort"
# "Quicksort"


# To get a surface from a rectangle, you can create a new Surface
# object using the rectangle's dimensions
# e.g. surf = pygame.Surface((a.w, a.h))
class NavigationBar:
    """Class to represent a navigation bar for the GUI."""

    def __init__(self, dimensions, elements, color):
        self.rectangle = pygame.Rect(dimensions)
        self.elements = elements
        self.color = color
        self.type = WidgetType.BAR

    def draw(self, surface):
        """Draw the navigation bar onto the screen."""
        label_x = 115
        label_y = 38
        pygame.draw.rect(surface, self.color, self.rectangle)
        for element in self.elements:
            if element.type == WidgetType.LABEL:
                element.draw(surface, (label_x, label_y))
                label_x += element.text.get_rect().right + 75
            else:
                element.draw(surface)

    def click(self, position):
        """Alter the state of the element in the navbar that
        was clicked.
        """
        pass

    def _get_surface(self):
        """Return the rectangular area of the navbar's area as
        a pygame Surface object."""
        return pygame.Surface(size=(self.rectangle.width, self.rectangle.height))


class NumberBar:
    """Class to represent a bar in the GUI. The bar in turns
    represents a number in a list.
    """

    def __init__(self, label, dimensions, color):
        self.rectangle = pygame.Rect(dimensions)
        self.label = label
        self.color = color
        self.type = WidgetType.BAR

    def draw(self, surface):
        """Draw the bar on the screen."""
        pygame.draw.rect(surface, self.color, self.rectangle)
        x = self.rectangle.left + self.rectangle.width // 2
        y = 560
        self.label.draw(surface, (x, y))

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
        return pygame.Surface(size=(self.rectangle.width, self.rectangle.height))


class NumberBarFactory:
    """Factory class to generate a collection of NumberBar instances."""

    background_color = (66, 134, 244, 0.8)  # blue
    font_color = (255, 255, 255)  # white
    scale_to_fit = 4.7

    @classmethod
    def create_bars(cls, surface, values, font_color=None, background_color=None):
        """Return NumberBar instances, each with one
        of the given values.
        """
        left = 280
        # space on the screen that should be occupied by the bars
        container_size = surface.get_width() - left * 2
        bar_width = container_size // len(values)
        font = pygame.font.SysFont(name="Arial", size=24)
        number_bars = []
        for value in values:
            number_label = Label(font, str(value), cls.font_color)
            bar_height = cls.scale_to_fit * value
            top = surface.get_height() - bar_height
            dimensions = (left, top, bar_width, bar_height)
            number_bar = NumberBar(
                number_label, dimensions, background_color or cls.background_color
            )
            number_bars.append(number_bar)
            left += (
                bar_width + bar_width // 10
            )  # add space between this bar and the next
        return number_bars

