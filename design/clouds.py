#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
clouds
-------

Functions for creating cloud graphics.
"""


from math import pi

from colors import rgb
from PIL import Image, ImageDraw

try:
    import cairo
except ImportError:
    import cairocffi as cairo


def draw_circle(ctx, x, y, radius, cairo_color):
    """
    Draw a circle.
    :param radius: radius in pixels
    :param cairo_color: normalized rgb color
    """
    ctx.new_path()
    ctx.set_source_rgb(cairo_color.red, cairo_color.green, cairo_color.blue)
    ctx.arc(x, y, radius, 0, 2 * pi)
    ctx.fill()


def draw_cloud(width=140, height=60, color=rgb(255, 255, 255)):
    """ Draw a cloud with the given width, height, and color. """

    cairo_color = color / rgb(255, 255, 255)

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    # A cloud consists of 4 circles
    draw_circle(ctx, width / 3, height / 2, height / 3, cairo_color)
    draw_circle(ctx, 2 * width / 3, height / 2, height / 3, cairo_color)
    draw_circle(ctx, width / 2, height / 3, height / 3, cairo_color)
    draw_circle(ctx, width / 2, 2 * height / 3, height / 3, cairo_color)

    surface.write_to_png('cloud.png')
