"""This module contains my implementation of bubble sort."""


import time


def bubble_sort(interface, sorting_speed):
    """Implementation of bubble sort. Bubble sort is a stable 
    sorting algorithm that sorts an unsorted list of elements 
    in-place.
    """
    bars = interface.bars
    num_bars = len(bars)
    for i in range(num_bars - 1):
        swapped = False
        for j in range(num_bars - i - 1):
            #color change to indicate a comparison being made
            bars[j].change_color("green")
            bars[j + 1].change_color("green")
            interface.render(bars[j], bars[j + 1])
            if bars[j] > bars[j + 1]:
                #color change to indicate a swap is about to occur
                bars[j].change_color("red")
                bars[j + 1].change_color("red")
                interface.render(bars[j], bars[j + 1])
                interface.swap(bars[j], bars[j + 1])
                swapped = True
            #change back to the original color
            if (not swapped and j + 1 == num_bars - i - 1) or i == num_bars - 2:
                break
            bars[j].change_color("blue")
            if j + 1 < num_bars - i - 1: #change only if it's in its sorted position
                bars[j + 1].change_color("blue")
            else:
                bars[j + 1].change_color("purple")
            interface.render(bars[j], bars[j + 1])
        if not swapped:
            break
    #change all bars to the final color to indicate the algorithm is finished
    interface.sorting_finished()


            