#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
borders
-------

Functions for creating border pattern graphics.
"""

# import cairo
from PIL import Image, ImageDraw

def circles(width=12, height=12):
    """
    Draws a repeatable white circle border pattern.
    """

    # surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    # ctx = cairo.Context(surface)
    # ctx.scale (width/1.0, height/1.0)

    image = Image.new("RGB", (width, height), color=None)
    draw = ImageDraw.Draw(image)
    draw.ellipse((0, 0, width - 1, height - 1), fill="white")
    image.save('circles.png')

if __name__ == '__main__':
    circles()