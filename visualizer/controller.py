"""This module contains the controller class for the sorting visualizer GUI."""


import sys
import pygame


class SortingVisualizerController:
    """Class to represent the controller for the visualizer."""

    def __init__(self, interface):
        self.interface = interface

    def run(self):
        """Start the visualizer."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if user clicked screen:
                    if navbar was clicked:
                        element = get_clicked_element()
                        if element is a sorting label:
                            #represents the button being selected. 
                            #Maybe it shoud maintain state as to whether is was clicked?
                            change_sorting_label_color() 
                            redraw_interface()
                        elif element is the one for changing array size:
                            change_array_size()
                            redraw_interface()
                        elif element is the on for changing sorting speed:
                            update_sorting_speed() #controller can maintain this. No redrawing necessary
                    else: #either the sort, reset button, or somewhere else on the screen were clicked
                        if sort button was clicked
                            if one of the sorting labels is highlighted
                                sort_bars_based_on_algorithm_selected()
                            else:
                                display_error_message() #need to select a sorting algorithm
                                redraw_interface()
                        elif reset button was clicked
                            generate_a_new_array() #reset the whole thing
                            redraw_interface()
                            

