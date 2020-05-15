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


def create_number_bars(screen, num_bars=5):
    """Create the bars that are going to represent numbers in an
    unsorted array.
    """
    number_bars = SortingVisualizerController.generate_new_array(screen, num_bars)
    return number_bars


def create_input_stepper(name, navbar_dimensions, button_color=(255, 255, 255)):
    """Create and return an input stepper widget."""
    #defaultbutton color is white
    font = pygame.font.SysFont(name="Arial", size=24)
    input_label = Label(font, "5", button_color)
    triangle_up = ()
    triangle_down = ()
    increment_button = InputStepperButton(triangle_up, button_color)
    decrement_button = InputStepperButton(triangle_down, button_color)
    input_stepper = InputStepper(
        input_label,
        increment_button,
        decrement_button,
        name
    )   
    return input_stepper


def create_navigation_bar(screen):
    """Create the navigation bar."""
    font = pygame.font.SysFont(name="Arial", size=24)
    font_color = (255, 255, 255) # white
    navbar_color = (51, 153, 255) # blue
    navbar_dimensions = (0, 0, screen.get_width(), screen.get_height() // 8)

    sorting_speed_widget = create_input_stepper("sorting_spped_adjuster", navbar_dimensions)
    array_size_widget = create_input_stepper("array_size_adjuster", navbar_dimensions)

    navbar_elements = [Label(font, algorithm, font_color) for algorithm in ALGORITHMS]
    navbar_elements.append(sorting_speed_widget)
    navbar_elements.append(array_size_widget)
    navbar_elements.append(Label(font, "Array Size", font_color))
    navbar_elements.append(Label(font, "Sorting Speed", font_color))

    navigation_bar = NavigationBar(navbar_dimensions, navbar_elements, navbar_color)
    return navigation_bar

    
def create_interface(screen):
    """Create all of the necessary shapes and objects
    to build the visualizer interface. Returns a
    SortingVisualizerGUI instance.
    """
    font = pygame.font.SysFont(name="Arial", size=24)
    font_color = (0, 0, 0) # black
    button_color = () # gray
    reset_buttons_dimensions = ()
    sort_button_dimensions = ()
    navigation_bar = create_navigation_bar(screen)
    sort_label = Label(font, "Sort", font_color)
    reset_label = Label(font, "Reset", font_color)

    reset_button = Button(reset_label, reset_button_dimensions, button_color)
    sort_button = Button(sort_label, sort_button_dimensions, button_color)

    number_bars = create_number_bars(screen)
    interface = SortingVisualizerGUI(
        screen,
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
    screen = pygame.display.set_mode(size=(width, height))
    screen.fill(background_color)

    interface = create_interface(screen)
    visualizer = create_controller(interface)
    visualizer.run()


if __name__ == "__main__":
    main()

