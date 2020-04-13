"""This module contains fixtures for testing the sorting
algorithm implmenttations."""


import pytest


class TestProduct:
    """Dummy class created to test the stability property of sorting algorithms."""

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __lt__(self, other):
        return self.quantity < other.quantity

    def __le__(self, other):
        return self.quantity <= other.quantity


@pytest.fixture
def empty_list():
    """Return an empty list."""
    return []


@pytest.fixture
def unsorted_list_of_integers():
    """Return an unsorted list of integers."""
    return [4, -7, 1, 10, 0, -1, -2]


@pytest.fixture
def sorted_list_of_integers():
    """Return a sorted list of integers."""
    return [0, 1, 2, 3, 4, 5]


@pytest.fixture
def list_of_objects():
    """Return a list of objects."""
    # used to test the stability of sorting algorithms
    test_products = [
        TestProduct("bread", 2),
        TestProduct("eggs", 10),
        TestProduct("milk", 10),
        TestProduct("cereal", 3),
        TestProduct("apples", 0),
        TestProduct("cheese", 1),
    ]
    return test_products

