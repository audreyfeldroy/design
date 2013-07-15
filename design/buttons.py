#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
buttons
-------

Functions for creating image and CSS buttons.
"""


from math import pi

from colors import rgb

try:
    import cairo
except ImportError:
    import cairocffi as cairo

from IPython import embed


def draw_img_button(width=200, height=50, text='This is a button', color=rgb(200,100,50)):
    """ Draws a simple image button. """
    
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)
    ctx.rectangle(0, 0, width - 1, height - 1)

    ctx.set_source_rgb(color.red/255.0, color.green/255.0, color.blue/255.0)
    ctx.fill()
    
    # Draw text
    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.select_font_face(
        "Helvetica",
        cairo.FONT_SLANT_NORMAL,
        cairo.FONT_WEIGHT_BOLD
    )
    ctx.set_font_size(15.0)
    ctx.move_to(15, 2 * height / 3)
    ctx.show_text(text)
    
    surface.write_to_png('button.png')
    

def draw_css_button(width=200, height=50, text='This is a button', color=rgb(200,100,50)):
    """ Draws a simple CSS button. """

    # TODO: once we've decided on a scss compiler, import it at the top instead
    from scss import Scss

    # TODO: make this customizable
    css_class = 'button'
    
    html = '<a class="{0}" href="TODO">{1}</a>'.format(css_class, text)
    
    css = Scss()
    scss_str = "a.{0} {{color: red + green;}}".format(css_class)
    css.compile(scss_str)

