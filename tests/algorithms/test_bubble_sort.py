"""This module contains tests for my bubble sort implementation."""


from algorithms.bubble_sort import bubble_sort


def test_sort_empty_list(empty_list):
    """Test that when bubble sort is passed an empty list,
    that nothing happens.
    """
    bubble_sort(empty_list)
    assert empty_list == []


def test_sort_unsorted_list_of_integers(unsorted_list_of_integers):
    """Test that when bubble sort is passed an unsorted list
    of integers that the list is properly sorted.
    """
    bubble_sort(unsorted_list_of_integers)
    assert [-7, -2, -1, 0, 1, 4, 10] == unsorted_list_of_integers


def test_sort_sorted_list_of_integers(sorted_list_of_integers):
    """Test that when bubble sort is passed a sorted list
    of integers that the list remains sorted.
    """
    bubble_sort(sorted_list_of_integers)
    assert [0, 1, 2, 3, 4, 5] == sorted_list_of_integers


def test_sort_is_stable(list_of_objects):
    """Test that if two elements in a list have the same key,
    that their relative ordering is still preserved after the
    list is sorted. This is achieved by using a list of objects,
    since you can sort the objects based on one attribute and
    then keep track of their ordering in the list through a second
    attribute.
    """
    bubble_sort(list_of_objects)
    
    #eggs should still come before milk in the list
    products = {}
    for index, obj in enumerate(list_of_objects):
        products[obj.name] = index
    assert products["eggs"] < products["milk"]
