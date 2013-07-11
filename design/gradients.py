#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
gradients
---------

Functions for creating gradient graphics.

.. note:: CSS3 gradients are better than image gradient strips in most cases.
    See http://www.colorzilla.com/gradient-editor/
"""

import cairo
from colors import rgb


def vertical_strip(width=10, height=100, color=rgb(100, 100, 100),
                   subtlety=0.1):
    """
    Draws a subtle vertical gradient strip.
    """

    cairo_color = color / rgb(255, 255, 255)

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    ctx.scale(width / 1.0, height / 1.0)

    pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
    pat.add_color_stop_rgba(
        0,
        cairo_color.red,
        cairo_color.green,
        cairo_color.blue,
        0
    )
    pat.add_color_stop_rgba(
        1,
        cairo_color.red,
        cairo_color.green,
        cairo_color.blue,
        1
    )

    ctx.rectangle(0, 0, 1, 1)
    ctx.set_source(pat)
    ctx.fill()

    surface.write_to_png('vertical_strip.png')


def vertical_white(width=10, height=100, subtlety=0.1):
    """
    Draws a subtle vertical gradient strip: white with varying alpha.
    """

    start = 0.5 - subtlety
    end = 0.5 + subtlety

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    ctx.scale(width/1.0, height/1.0)

    pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
    pat.add_color_stop_rgba(0, 1, 1, 1, start)
    pat.add_color_stop_rgba(1, 1, 1, 1, end)

    ctx.rectangle(0, 0, 1, 1)
    ctx.set_source(pat)
    ctx.fill()

    surface.write_to_png('vertical_white.png')
