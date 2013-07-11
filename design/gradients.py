#!/usr/bin/env python

import math
import cairo

# def color_to_range(color, offset):
#     """
#     Turns a color tuple into a color range list.
#     """
#     color1 = color - [offset, offset, offset]


def vertical_strip(width=10, height=100, color=[100, 100, 100], subtlety=0.1):
    """
    Draws a subtle vertical gradient strip.
    """

    red = color[0] / 255.0
    green = color[1] / 255.0
    blue = color[2] / 255.0

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    ctx.scale (width/1.0, height/1.0)

    pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
    pat.add_color_stop_rgba(0, red, green, blue, 0)
    pat.add_color_stop_rgba(1, red, green, blue, 1)

    ctx.rectangle(0,0,1,1)
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

    ctx.scale (width/1.0, height/1.0)

    pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
    pat.add_color_stop_rgba(0, 1, 1, 1, start)
    pat.add_color_stop_rgba(1, 1, 1, 1, end)

    ctx.rectangle(0,0,1,1)
    ctx.set_source(pat)
    ctx.fill()

    surface.write_to_png('vertical_white.png')
