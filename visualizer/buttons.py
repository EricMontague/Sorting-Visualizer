"""This module contains the class responsible for defining buttons."""

# https://inventwithpython.com/blog/2012/10/30/designing-a-button-ui-module-for-pygame/
import pygame
from visualizer.widget_types import WidgetType


# Buttons:
# "Reset"
# "Sort!"

# "Speed": button with a triangle in the middle and a number on the side
# "Array Size": button with a triangle in the middle


class Button:
    """Class to represent a button."""

    def __init__(self, label, dimensions, background_color):
        self.rectangle = pygame.Rect(dimensions)
        self.label = label
        self.background_color = background_color
        self.type = WidgetType.BUTTON

    def draw(self, surface):
        """Draw the button."""
        pygame.draw.rect(surface, self.background_color, self.rectangle)
        self.label.draw(surface, self.rectangle.center)

    def undraw(self):
        """Undraw the button."""
        pass

    def clicked(self, mouse_position):
        """Return True if the user clicked the button."""
        return self.rectangle.collidepoint(mouse_position)

    def activate(self):
        """Highlight this button to show that it has been
        selected.
        """
        pass

    def deactivate(self):
        """Unhighlight this button to show that it is not selected."""
        pass

    def get_label(self):
        """Return the text label for the button."""
        pass

    @property
    def name(self):
        """Return the button label's text."""
        return self.label.name

    def _get_surface(self):
        """Return the rectangular area of the navbar's area as
        a pygame Surface object."""
        return pygame.Surface(size=(self.rectangle.width, self.rectangle.height))


# https://www.nngroup.com/articles/input-steppers/
class InputStepperButton:
    """Class to represent either a minus or plus button for
    an input stepper widget.
    """

    def __init__(self, points, background_color, line_width=0):
        self.points = points
        self.background_color = background_color
        self.line_width = line_width
        self.type = WidgetType.BUTTON

    def draw(self, surface):
        """Draw the button onto the given surface."""
        self.triangle = pygame.draw.polygon(
            surface, self.background_color, self.points, self.line_width
        )

    def clicked(self, mouse_position):
        """Return True if the button was clicked, else return False."""
        return self.triangle.collidepoint(mouse_position)

    @property
    def center(self):
        """Return the center of the button as a tuple containing
        the center's x and y coordinates.
        """
        return (self.center_x, self.center_y)

    @property
    def center_x(self):
        """Return the x-coordinate of the button's centerpoint."""
        return max(self.points[0])

    @property
    def center_y(self):
        """Return the y-coordinate of the buttons' centerpoint."""
        y_coords = set()
        for point in self.points:
            y_coords.add(point[1])
        return sum(y_coords) // len(y_coords)
