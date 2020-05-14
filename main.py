"""This script contains the main function for the sorting visualizer."""


import pygame
from visualizer import SortingVisualizerGUI
from visualizer import SortingVisualizerController
from visualizer.bars import NumberBar, NavigationBar
from visualizer.buttons import Button, InputStepperButton
from visualizer.labels import Label
from visualizer.widgets import InputStepper
from algorithms import ALGORITHMS



def create_controller(interface):
    """Initialize and return the visualizer controller."""
    visualizer = SortingVisualizerController(interface, ALGORITHMS)
    return visualizer


def create_number_bars(window, num_bars=5):
    """Create the bars that are going to represent numbers in an
    unsorted array.
    """
    number_bars = SortingVisualizerController.generate_new_array(window, num_bars)
    return number_bars


def create_input_stepper(name, navbar):
    """Create and return an input stepper widget."""
    
    minus_button_center = ()
    plus_button_center = ()
    input_label = Label()
    minus_label = Label()
    plus_label = Label()
    increment_button = InputStepperButton(plus_button_center, plus_label)
    decrement_button = InputStepperButton(minus_button_center, minus_label)
    input_stepper = InputStepper(
        input_label,
        increment_button,
        decrement_button,
        name
    )   
    return input_stepper


def create_navigation_bar(window):
    """Create the navigation bar."""
    navbar_color = "blue"
    dimensions = (1,2,3,4)
    navbar = pygame.draw.rect(window, navbar_color, dimensions)
    sorting_speed_widget = create_input_stepper("sorting_spped_adjuster", navbar)
    array_size_widget = create_input_stepper("array_size_adjuster", navbar)
    navbar_elements = [Label() for algorithm in ALGORITHMS]
    navbar_elements.append(sorting_speed_widget)
    navbar_elements.append(array_size_widget)
    navigation_bar = NavigationBar(navbar, navbar_elements)
    return navigation_bar

    
def create_interface(window):
    """Create all of the necessary shapes and objects
    to build the visualizer interface. Returns a
    SortingVisualizerGUI instance.
    """
    navigation_bar = create_navigation_bar(window)
    reset_button = Button()
    sort_button = Button()
    number_bars = create_number_bars(window)
    interface = SortingVisualizerGUI(
        navigation_bar,
        [reset_button, sort_button],
        number_bars
    )
    return interface


def main():
    """Start the sorting visualizer."""
    pygame.init()
    width = 1080
    height = 600
    background_color = (255, 255, 255) # white
    window = pygame.display.set_mode(size=(width, height))
    window.fill(background_color)
    interface = create_interface(window)
    visualizer = create_controller(interface)
    visualizer.run()


if __name__ == "__main__":
    main()

