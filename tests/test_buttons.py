#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_buttons
------------

Tests for `design.buttons` module.
"""

import imghdr
import os
import unittest

from design import buttons
from colors import rgb

class TestButtons(unittest.TestCase):

    def test_draw_button(self):
        buttons.draw_img_button(
            width=176,
            height=28,
            text='Please push me :)',
            color=rgb(53,166,193)
        )
        self.assertEqual(imghdr.what('button.png'), 'png')

    @classmethod
    def tearDownClass(cls):
        os.remove('button.png')

if __name__ == '__main__':
    unittest.main()
