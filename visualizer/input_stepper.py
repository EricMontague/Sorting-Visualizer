"""This module contains an input stepper to be used in the sorting visualizer."""


import pygame
from visualizer.widget_types import WidgetType
from visualizer.labels import Label


class InputStepper:
    """Class to represent an input stepper."""

    def __init__(
        self, text_label, value_label, increment_button, decrement_button, name
    ):
        self.text_label = text_label
        self.value_label = value_label
        self.increment_button = increment_button
        self.decrement_button = decrement_button
        self.name = name
        self.type = WidgetType.INPUT_STEPPER

    def draw(self, surface):
        """Draw the widget on the screen."""
        value_x = self.increment_button.center_x + 30
        value_y = (self.increment_button.center_y + self.decrement_button.center_y) // 2
        self.value_label.draw(surface, (value_x, value_y))

        text_x = value_x - 110
        text_y = value_y
        self.text_label.draw(surface, (text_x, text_y))
        self.increment_button.draw(surface)
        self.decrement_button.draw(surface)

    def clicked(self, mouse_position):
        """Return True if one of the buttons of the input stepper
        was clicked."""
        return self.increment_button.clicked(
            mouse_position
        ) or self.decrement_button.clicked(mouse_position)

    def update(self, mouse_position, current_value):
        """Update the value displayed by the widget
        depending on which button was clicked.
        """
        font = pygame.font.SysFont(name="Arial", size=24)
        if self.increment_button.clicked(mouse_position) and current_value < 30:
            self.value_label = Label(font, current_value + 5, self.value_label.font_color)
        elif self.decrement_button.clicked(mouse_position) and current_value >= 5:
            self.value_label = Label(font, current_value - 5, self.value_label.font_color)
            
