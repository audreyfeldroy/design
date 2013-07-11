#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
borders
-------

Functions for creating border pattern graphics.
"""

from math import pi

import cairo
from colors import rgb
from PIL import Image, ImageDraw


def circles_pil(width, height, color):
    """ Implementation of circle border with PIL. """

    image = Image.new("RGBA", (width, height), color=None)
    draw = ImageDraw.Draw(image)
    draw.ellipse((0, 0, width - 1, height - 1), fill=color)
    image.save('circles.png')

def circles_pycairo(width, height, color):
    """ Implementation of circle border with PyCairo. """

    cairo_color = color / rgb(255, 255, 255)

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    # draw a circle in the center
    ctx.new_path()
    ctx.set_source_rgb(cairo_color.red, cairo_color.green, cairo_color.blue)  # blue
    ctx.arc(width / 2, height / 2, width / 2, 0 , 2 * pi)
    ctx.fill()  # stroke current path

    # save to PNG
    surface.write_to_png('circles.png')

def circles(width=12, height=12, color=rgb(255, 255, 255)):
    """ Draws a repeatable circle border pattern. """

    circles_pycairo(width, height, color)


if __name__ == '__main__':
    circles()
