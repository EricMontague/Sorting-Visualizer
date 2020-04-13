"""This module contains fixtures for testing the sorting
algorithm implmenttations."""


import pytest


class TestProduct:
    """Dummy class created to test the stability 
    property of sorting algorithms.
    """

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __lt__(self, other):
        return self.quantity < other.quantity

    def __le__(self, other):
        return self.quantity <= other.quantity

    def __eq__(self, other):
        return self.quantity == other.quantity


@pytest.fixture
def empty_list():
    """Return an empty list."""
    empty_list = []
    return empty_list


@pytest.fixture
def unsorted_list_of_integers():
    """Return an unsorted list of integers."""
    unsorted_list = [4, -7, 1, 10, 0, -1, -2]
    return unsorted_list


@pytest.fixture
def sorted_list_of_integers():
    """Return a sorted list of integers."""
    sorted_list = [-7, -2, -1, 0, 1, 4, 10]
    return sorted_list


@pytest.fixture
def unsorted_list_of_products():
    """Return a list of product objects. Products are sorted on their
    quantity attribute. Used to test the stability 
    of sorting algorithms.
    """
    test_products = [
        TestProduct("bread", 2),
        TestProduct("eggs", 10),
        TestProduct("milk", 10),
        TestProduct("cereal", 3),
        TestProduct("apples", 0),
        TestProduct("cheese", 1),
    ]
    return test_products


@pytest.fixture
def sorted_list_of_products_stable():
    """Return a list of product objects, where the relative ordering
    of elements is preserved.
    """
    #Eggs appears before milk in the unsorted fixture, so you should
    #expect that it also appears before milk in the sorted output
    test_products = [
        TestProduct("apples", 0),
        TestProduct("cheese", 1),
        TestProduct("bread", 2),
        TestProduct("cereal", 3),
        TestProduct("eggs", 10),
        TestProduct("milk", 10),
    ]
    return test_products


@pytest.fixture
def sorted_list_of_products_unstable():
    """Return a list of product objects, where the relative ordering
    of elements is not preserved.
    """
    #Eggs appears before milk in the unsorted fixture, but in an
    #unstable sorting algorithm, this may not be the case for the ouput
    test_products = [
        TestProduct("apples", 0),
        TestProduct("cheese", 1),
        TestProduct("bread", 2),
        TestProduct("cereal", 3),
        TestProduct("milk", 10),
        TestProduct("eggs", 10),
    ]
    return test_products
