"""This module contains my implementation of bubble sort."""


def bubble_sort(unsorted_list):
    """Implementation of bubble sort. Bubble sort is 
    a stable sorting algorithm that sorts an 
    unsorted list of elements in-place."""
    for i in range(len(unsorted_list) - 1):
        swapped = False
        for j in range(len(unsorted_list) - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True
        if not swapped:
            break
            