#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_gradients
--------------

Tests for `design.gradients` module.
"""

import imghdr
import os
import unittest

from colors import rgb
from design import gradients


class TestGradients(unittest.TestCase):

    def test_vertical_strip(self):
        gradients.vertical_strip(width=10, height=107,
                                 color=rgb(255, 252, 229))
        self.assertEqual(imghdr.what('vertical_strip.png'), 'png')

    def test_vertical_white(self):
        gradients.vertical_white(width=10, height=107)
        self.assertEqual(imghdr.what('vertical_white.png'), 'png')

    @classmethod
    def tearDownClass(cls):
        os.remove('vertical_strip.png')
        os.remove('vertical_white.png')

if __name__ == '__main__':
    unittest.main()
