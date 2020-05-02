"""This module contains the class responsible for calling the sorting algorithm
requested by the user."""



class SortManager:
    """Class responsible for calling the sorting algorithm 
    requested by the user.
    """

    def __init__(self, algorithm):
        # algorithm is a function that implements a sorting algorithm
        self.algorithm = algorithm

    def sort(self, unsorted_list):
        """Given an unsorted list, sort the list using the algorithm
        defined in the algorithm attribute. Return the sorted list.
        """
        return self.algorithm(unsorted_list)
        
