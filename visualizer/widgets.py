"""This module contains widgets to be used in the sorting visualizer."""


import pygame


class InputStepper:
    """Class to represent an input stepper."""
    
    def __init__(self, label, increment_button, decrement_button, name):
        self.label = label
        self.increment_button = increment_button
        self.decrement_button = decrement_button
        self.name = name

    def draw(self, surface):
        """Draw the widget on the screen."""
        self.label.draw(surface)
        self.increment_button.draw(surface)
        self.decrement_button.draw(surface)

    def undraw(self):
        """Undraw the widget."""
        pass

    def update(self, mouse_position):
        """Update the value displayed by the widget
        depending on which button was clicked.
        """
        pass

