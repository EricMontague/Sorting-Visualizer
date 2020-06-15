"""This module contains views for the sorting visualizer GUI."""


import pygame
import sys
import time
from visualizer.widget_types import WidgetType
from visualizer.labels import Label


RED = (244, 66, 146)


class SortingVisualizerGUI:
    """Class to represent the main GUI view for the visualizer."""

    def __init__(self, screen, navbar, buttons, bars):
        self.screen = screen
        self.navbar = navbar
        self.buttons = buttons
        self.bars = bars
        self.navbar.draw(self.screen)
        for button in self.buttons:
            button.draw(self.screen)
        pygame.display.flip()

    def get_clicked_element(self):
        """Return the element on the screen that was clicked by the user."""
        elements = self.navbar.elements + self.buttons
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    for element in elements:
                        if element.clicked(position):
                            return element, position

    def draw_bars(self, bars):
        """Draw the number bars onto the screen."""
        draw_labels = True
        if len(bars) >= 20:
            draw_labels = False
        for bar in bars:
            bar.draw(self.screen, draw_labels)

    def render(self, **kwargs):
        """Draw the given elements on the screen."""
        if "input_stepper" in kwargs:
            kwargs["input_stepper"].draw(self.screen)
        if "algorithm" in kwargs:
            kwargs["algorithm"].draw(self.screen)
        if "bars" in kwargs:
            self.draw_bars(kwargs["bars"])

    def display_message(self, message, coordinates, color=RED):
        """Display the given message on the screen."""
        font = pygame.font.SysFont(name="Arial", size=24)
        error_message = Label(font, message, color)
        error_message.draw(self.screen, coordinates)

        # pause for two seconds before clearing error message
        time.sleep(2)

        background_color = self.screen.get_at(coordinates)
        error_message = Label(font, message, background_color)
        error_message.draw(self.screen, coordinates)

    def swap(self, bar_one, bar_two):
        """Swap both of the given bars' positions."""
        # both bars will be red when this method is called.
        # first, swap them
        # next, turn them green to indicate they've been swapped
        bar_one.top, bar_two.top = bar_two.top, bar_one.top

        # swap labels
        bar_one.label, bar_two.label = bar_two.label, bar_one.label

        # change color
        bar_one.change_color(GREEN)
        bar_two.change_color(GREEN)
        self.render(bars=[bar_one, bar_two])

    def sorting_finish(self):
        """Change the colors of all of the bars to indicate
        that they are sorted.
        """
        # change them to green first and then to purple
        for bar in self.bars:
            bar.change_color(GREEN)
        self.render(bars=self.bars)

        time.sleep(2)

        for bar in self.bars:
            bar.change_color(PURPLE)
        self.render(bars=self.bars)

