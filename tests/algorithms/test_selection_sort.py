"""This module contains tests for my implementation of selection sort."""


from algorithms import selection_sort


def test_sort_empty_list(empty_list):
    """Test that when selection sort is passed an empty list,
    that nothing happens.
    """
    selection_sort(empty_list)
    assert empty_list == []


def test_sort_unsorted_list_of_integers(
    unsorted_list_of_integers, sorted_list_of_integers
):
    """Test that when selection sort is passed an unsorted list
    of integers that the list is properly sorted.
    """
    selection_sort(unsorted_list_of_integers)
    assert unsorted_list_of_integers == sorted_list_of_integers


def test_sort_sorted_list_of_integers(sorted_list_of_integers):
    """Test that when selection sort is passed a sorted list
    of integers that the list remains sorted.
    """
    selection_sort(sorted_list_of_integers)
    assert sorted_list_of_integers == [-7, -2, -1, 0, 1, 4, 10]


def test_selection_sort_is_stable_must_fail(
    unsorted_list_of_products, sorted_list_of_products_unstable
):
    """Test that if two elements in a list have the same key,
    that their relative ordering is still preserved after the
    list is sorted. Selection sort is not a stable sorting algorithm,
    so this test should fail. This is achieved by using a list of objects,
    since you can sort the objects based on one attribute and
    then keep track of their ordering in the list through a second
    attribute.
    """
    selection_sort(unsorted_list_of_products)
    assert unsorted_list_of_products == sorted_list_of_products_unstable
