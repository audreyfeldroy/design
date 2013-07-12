=====
Usage
=====

Still Pre-Alpha
---------------

This isn't ready to use yet, but you could imagine something like this::

    from colors import rgb
    from design import buttons

    buttons.make_arrow_button(
        width=120,
        height=30,
        color=rgb(255, 129, 190),
        push_depth=8,
        glow_on_hover=True
    )

The above would result in these files being generated:

    * img/arrow.png
    * css/arrow.css  (Or maybe a Compass file. Haven't decided yet.)
    * js/arrow.js
    * arrow.html (Demo of the arrow in action.)

Ideas/feedback? File an issue!