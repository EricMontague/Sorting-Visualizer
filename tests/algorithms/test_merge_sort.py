"""This module contains tests for my implementation of merge sort."""


from algorithms import merge_sort
from algorithms.merge_sort import merge


def test_merge_sorted_list():
    """Test that the merge function will properly merge two child
    lists into their parent when given a sorted parent list.
    """
    left = [1, 2]
    right = [4, 5]
    parent = [1, 2, 4, 5]
    merge(parent, left, right)
    # parent list should remain sorted
    assert parent == [1, 2, 4, 5]


def test_merge_unsorted_list():
    """Test that the merge function will properly merge two child
    lists into their parent when given an unsorted parent list.
    """
    left = [1, 2]
    right = [4, 5]
    parent = [5, 2, 1, 4]
    merge(parent, left, right)
    # parent list should be sorted
    assert parent == [1, 2, 4, 5]


def test_sort_empty_list(empty_list):
    """Test that when merge sort is passed an empty list,
    that nothing happens.
    """
    merge_sort(empty_list)
    assert empty_list == []


def test_sort_unsorted_list_of_integers(
    unsorted_list_of_integers, sorted_list_of_integers
):
    """Test that when merge sort is passed an unsorted list
    of integers that the list is properly sorted.
    """
    merge_sort(unsorted_list_of_integers)
    assert unsorted_list_of_integers == sorted_list_of_integers


def test_sort_sorted_list_of_integers(sorted_list_of_integers):
    """Test that when merge sort is passed a sorted list
    of integers that the list remains sorted.
    """
    merge_sort(sorted_list_of_integers)
    assert sorted_list_of_integers == [-7, -2, -1, 0, 1, 4, 10]


def test_merge_sort_is_stable(
    unsorted_list_of_products, sorted_list_of_products_stable
):
    """Test that if two elements in a list have the same key,
    that their relative ordering is still preserved after the
    list is sorted. This is achieved by using a list of objects,
    since you can sort the objects based on one attribute and
    then keep track of their ordering in the list through a second
    attribute.
    """
    merge_sort(unsorted_list_of_products)
    assert unsorted_list_of_products == sorted_list_of_products_stable
