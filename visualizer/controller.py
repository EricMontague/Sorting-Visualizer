"""This module contains the controller class for the sorting visualizer GUI."""


import pygame
import random
from visualizer.bars import NumberBarFactory


class SortingVisualizerController:
    """Class to represent the controller for the visualizer."""

    def __init__(self, interface, algorithms, sorting_speed=5, array_size=5):
        self.interface = interface
        self.algorithms = algorithms
        self.sorting_speed = sorting_speed
        self.selected_algorithm = None
        self.array_size = array_size

    def run(self):
        """Start the visualizer."""
        while True:
            element, mouse_position = self.interface.get_clicked_element()
            if element.name in self.algorithms:
                self.selected_algorithm = element.actual_text
                element.change_color(PURPLE)
                self.interface.render(algorithm=element)
            elif element.name == "sorting_speed_adjuster":
                element.update(mouse_position, self.sorting_speed)
                self.interface.navbar.render(input_stepper=element)
            elif element.name == "array_size_adjuster":
                element.update(mouse_position, self.array_size)
                new_number_bars = SortingVisualizerController.generate_new_array(
                    self.interface.screen, element.value
                )
                self.update_array_size(len(new_number_bars))
                self.interface.render(bars=new_number_bars, input_stepper=element)
            elif element.name == "sort_button":
                if self.is_algorithm_selected():  # Run selected algorithm
                    sort = self.algorithms[self.selected_algorithm]
                    sort(self.interface, self.sorting_speed)
                else:
                    message = "Please choose an algorithm."
                    self.interface.display_message(
                        message,
                        (
                            self.interface.width * 0.5,
                            self.interface.height * 0.8,
                        ),
                    )
            elif element.name == "reset_button":
                self.reset()

    def update_selected_algorithm(self, algorithm):
        """Update the selected algorithm attribute."""
        self.selected_algorithm = algorithm

    def update_sorting_speed(self, speed):
        """Update the registered sorting speed."""
        self.sorting_speed = speed

    def update_array_size(self, num_bars):
        """Update the registered number of bars on the screen."""
        self.array_size = num_bars

    @staticmethod
    def generate_new_array(surface, size):
        """Return a new list of bars of the given size and to replace
        the bars currently on the screen.
        """
        values = [random.randrange(20, 100) for num in range(size)]
        number_bars = NumberBarFactory.create_bars(surface, values)
        return number_bars

    def is_algorithm_selected(self):
        """Return True if the user has selected an algorithm."""
        return self.selected_algorithm is not None

    def reset(self):
        """Reset the GUI back to its original state."""
        new_number_bars = SortingVisualizerController.generate_new_array(
            self.interface.screen, self.array_size
        )
        self.interface.render(bars=new_number_bars)

