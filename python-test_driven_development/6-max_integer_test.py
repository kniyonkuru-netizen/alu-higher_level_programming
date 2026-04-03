#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test with a list sorted in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with the max integer at the beginning."""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_middle(self):
        """Test with the max integer in the middle."""
        self.assertEqual(max_integer([1, 5, 9, 3, 2]), 9)

    def test_max_at_end(self):
        """Test with the max integer at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_single_element(self):
        """Test with a single element list."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """Test with no argument uses default empty list."""
        self.assertIsNone(max_integer())

    def test_all_negative(self):
        """Test with all negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_single_negative(self):
        """Test with a single negative element."""
        self.assertEqual(max_integer([-5]), -5)

    def test_mixed_positive_negative(self):
        """Test with a mix of positive and negative integers."""
        self.assertEqual(max_integer([-10, 0, 5, -3]), 5)

    def test_all_same_values(self):
        """Test with all elements equal."""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_two_elements(self):
        """Test with exactly two elements."""
        self.assertEqual(max_integer([4, 3]), 4)
        self.assertEqual(max_integer([3, 6]), 6)

    def test_descending_order(self):
        """Test with a list sorted in descending order."""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_with_zero(self):
        """Test with zero in the list."""
        self.assertEqual(max_integer([0, -1, -2]), 0)

    def test_zero_only(self):
        """Test with a list containing only zero."""
        self.assertEqual(max_integer([0]), 0)

    def test_large_numbers(self):
        """Test with very large integers."""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)

    def test_large_list(self):
        """Test with a large list."""
        large = list(range(1, 1001))
        self.assertEqual(max_integer(large), 1000)

    def test_returns_correct_type(self):
        """Test that the return type is int."""
        self.assertIsInstance(max_integer([1, 2, 3]), int)

    def test_none_return_on_empty(self):
        """Test that None is returned (not 0 or False) on empty list."""
        result = max_integer([])
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
