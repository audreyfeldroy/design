#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_clouds
--------------

Tests for `design.clouds` module.
"""

import imghdr
import os
import unittest

from design import clouds


class TestClouds(unittest.TestCase):

    def test_draw_cloud(self):
        clouds.draw_cloud()
        self.assertEqual(imghdr.what('cloud.png'), 'png')

    @classmethod
    def tearDownClass(cls):
        os.remove('cloud.png')

if __name__ == '__main__':
    unittest.main()
