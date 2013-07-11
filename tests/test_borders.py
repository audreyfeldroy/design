#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_borders
------------

Tests for `design.borders` module.
"""

import imghdr
import os
import unittest

from design import borders


class TestBorders(unittest.TestCase):

    def test_circles(self):
        borders.circles(width=10, height=10)
        self.assertEqual(imghdr.what('circles.png'), 'png')

    @classmethod
    def tearDownClass(cls):
        # os.remove('circles.png')

if __name__ == '__main__':
    unittest.main()
