"""This script contains the main function for the sorting visualizer."""


import pygame
from visualizer import SortingVisualizerGUI
from visualizer import SortingVisualizerController
from visualizer.bars import NumberBar, NavigationBar
from visualizer.buttons import Button, InputStepperButton
from visualizer.labels import Label
from visualizer.input_stepper import InputStepper
from algorithms import ALGORITHMS


WHITE = (255, 255, 255)
GRAY = (230, 230, 230)
BLACK = (0, 0, 0)
PURPLE = (98, 110, 227)
NAVY_BLUE = (52, 73, 94)


def create_controller(interface):
    """Initialize and return the visualizer controller."""
    visualizer = SortingVisualizerController(interface, ALGORITHMS)
    return visualizer


def create_number_bars(screen, num_bars=30):
    """Create the bars that are going to represent numbers in an
    unsorted array.
    """
    number_bars = SortingVisualizerController.generate_new_array(screen, num_bars)
    return number_bars


def create_input_stepper(
    name, navbar_dimensions, triangle_up, triangle_down, color=NAVY_BLUE
):
    """Create and return an input stepper widget."""
    font = pygame.font.SysFont(name="Arial", size=24)
    value_label = Label(font, "5", color)
    text_label = Label(font, name, color)

    increment_button = InputStepperButton(triangle_up, color)
    decrement_button = InputStepperButton(triangle_down, color)
    input_stepper = InputStepper(
        text_label,
        value_label,
        increment_button,
        decrement_button,
        name.lower().replace(" ", "_") + "_adjuster",
    )
    return input_stepper


def create_navigation_bar(screen):
    """Create the navigation bar."""
    font = pygame.font.SysFont(name="Arial", size=24)
    navbar_dimensions = (0, 0, screen.get_width(), screen.get_height() // 8)

    sorting_speed_widget = create_input_stepper(
        "Sorting Speed",
        navbar_dimensions,
        [(1000, 110), (990, 120), (1010, 120)],
        [(1000, 135), (990, 125), (1010, 125)],
    )
    array_size_widget = create_input_stepper(
        "Array Size",
        navbar_dimensions,
        [(1000, 150), (990, 160), (1010, 160)],
        [(1000, 175), (990, 165), (1010, 165)],
    )

    navbar_elements = [Label(font, algorithm, WHITE) for algorithm in ALGORITHMS]
    navbar_elements.append(sorting_speed_widget)
    navbar_elements.append(array_size_widget)

    navigation_bar = NavigationBar(navbar_dimensions, navbar_elements, NAVY_BLUE)
    return navigation_bar


def create_interface(screen):
    """Create all of the necessary shapes and objects
    to build the visualizer interface. Returns a
    SortingVisualizerGUI instance.
    """
    # need to consider putting the center variable back in the label constructor
    # can't draw a surface on another surface
    font = pygame.font.SysFont(name="Arial", size=24)
    reset_button_dimensions = (65, 100, 100, 50)
    sort_button_dimensions = (65, 160, 100, 50)
    navigation_bar = create_navigation_bar(screen)
    sort_label = Label(font, "Sort", WHITE)
    reset_label = Label(font, "Reset", WHITE)

    reset_button = Button(reset_label, reset_button_dimensions, PURPLE)
    sort_button = Button(sort_label, sort_button_dimensions, PURPLE)

    number_bars = create_number_bars(screen)
    interface = SortingVisualizerGUI(
        screen, navigation_bar, [reset_button, sort_button], number_bars
    )
    return interface


def main():
    """Start the sorting visualizer."""
    pygame.init()
    width = 1080
    height = 600
    screen = pygame.display.set_mode(size=(width, height))
    screen.fill(GRAY)

    interface = create_interface(screen)
    visualizer = create_controller(interface)
    visualizer.run()


if __name__ == "__main__":
    main()

