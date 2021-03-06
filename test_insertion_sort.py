#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import numpy as np
from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_empty(self):
        a = np.array([])
        b = insertion_sort(a)
        self.assertTrue(np.array_equal(b, []))

    def test_one(self):
        a = np.array([1])
        b = insertion_sort(a)
        self.assertTrue(np.array_equal(b, [1]))

    def test_two(self):
        a = np.array([1, 0])
        b = insertion_sort(a)
        self.assertTrue(np.array_equal(b, [0, 1]))

    def test_five(self):
        a = np.array([2, 1, 0, -1, -2])
        b = insertion_sort(a)
        self.assertTrue(np.array_equal(b, [-2, -1, 0, 1, 2]))


if __name__ == '__main__':
    unittest.main()
