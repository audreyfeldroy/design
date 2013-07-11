#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
borders
-------

Functions for creating border pattern graphics.
"""

from PIL import Image, ImageDraw

def circles(width=12, height=12, color="white"):
    """
    Draws a repeatable circle border pattern.
    """

    image = Image.new("RGBA", (width, height), color=None)
    draw = ImageDraw.Draw(image)
    draw.ellipse((0, 0, width - 1, height - 1), fill=color)
    image.save('circles.png')

if __name__ == '__main__':
    circles()
