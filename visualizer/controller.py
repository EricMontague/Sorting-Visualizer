"""This module contains the controller class for the sorting visualizer GUI."""


import sys
import pygame
import random
from visualizer.bars import NumberBarFactory


class SortingVisualizerController:
    """Class to represent the controller for the visualizer."""

    def __init__(self, interface, algorithms, sorting_speed=5):
        self.interface = interface
        self.algorithms = algorithms
        self.sorting_speed = sorting_speed
        self.selected_algorithm = None

    def run(self):
        """Start the visualizer."""
        while not self.interface.quit():
            element, mouse_position = self.interface.get_clicked_element()
            if element.name in self.algorithms:
                self.update_selected_algorithm(element.name)
                self.interface.navbar.choose_algorithm(element.name)
                self.interface.render(self.interface.navbar)
            elif element.name == "speed_adjuster":
                self.update_sorting_speed(element.value)
                element.update(mouse_position)
                self.interface.navbar.render(element)
            elif element.name == "array_size_adjuster":
                element.update(mouse_position)
                new_array = SortingVisualizerController.generate_new_array(element.value)
                self.interface.render(new_array, element)
            elif element.name == "sort_button":
                if self.is_algorithm_selected():
                    sort = self.algorithms[self.selected_algorithm]
                    sort(self.interface, self.sorting_speed)
                else:
                    message = "Please choose an algorithm."
                    self.interface.display_message(
                        message, 
                        coordinates=(
                            self.interface.width * 0.5,
                            self.interface.height * 0.8,
                        )
                    )
            elif element.name == "reset_button":
                self.reset()
        sys.exit()

    def update_selected_algorithm(self, algorithm):
        """Update the selected algorithm attribute."""
        self.selected_algorithm = algorithm
    
    def update_sorting_speed(self, speed):
        """Update the registered sorting speed."""
        pass
    
    @staticmethod
    def generate_new_array(surface, size):
        """Return a new list of bars of the given size and to replace
        the bars currently on the screen.
        """
        values = [random.randrange(1, 100) for num in range(size)]
        number_bars = NumberBarFactory.create_bars(surface, values)
        return number_bars

    def is_algorithm_selected(self):
        """Return True if the user has selected an algorithm."""
        return self.selected_algorithm is not None
    
    def reset(self):
        """Reset the GUI back to its original state."""
        pass


