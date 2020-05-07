"""This package contains various sorting alorithms to be used in the
visualizer GUI.
"""


from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quicksort import quicksort
from algorithms.heapsort import heapsort


ALGORITHMS = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quicksort": quicksort,
    "Heapsort": heapsort
}


