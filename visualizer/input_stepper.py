"""This module contains an input stepper to be used in the sorting visualizer."""


import pygame
from visualizer.widget_types import WidgetType


class InputStepper:
    """Class to represent an input stepper."""

    def __init__(self, label, increment_button, decrement_button, name):
        self.label = label
        self.increment_button = increment_button
        self.decrement_button = decrement_button
        self.name = name
        self.type = WidgetType.INPUT_STEPPER

    def draw(self, surface):
        """Draw the widget on the screen."""
        x = self.increment_button.center_x - 30
        y = (self.increment_button.center_y + self.decrement_button.center_y) // 2
        self.label.draw(surface, (x, y))
        self.increment_button.draw(surface)
        self.decrement_button.draw(surface)

    def undraw(self):
        """Undraw the widget."""
        pass

    def clicked(self, mouse_position):
        """Return True if one of the buttons of the input stepper
        was clicked."""
        return (
            self.increment_button.clicked(mouse_position) 
            or self.decrement_button.clicked(mouse_position)
        )

    def update(self, mouse_position):
        """Update the value displayed by the widget
        depending on which button was clicked.
        """
        pass

