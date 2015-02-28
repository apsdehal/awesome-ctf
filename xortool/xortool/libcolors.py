#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os


BASH_ATTRIBUTES = {"regular": "0",
                   "bold": "1", "underline": "4", "strike": "9",
                   "light": "1", "dark": "2",
                   "invert": "7"}  # invert bg and fg

BASH_COLORS = {"black": "30", "red": "31", "green": "32", "yellow": "33",
               "blue": "34", "purple": "35", "cyan": "36", "white": "37"}

BASH_BGCOLORS = {"black": "40", "red": "41", "green": "42", "yellow": "43",
                 "blue": "44", "purple": "45", "cyan": "46", "white": "47"}


def _main():
    header = color("white", "black", "dark")
    print

    print header + "       " + "Colors and backgrounds:      " + color()
    for c in _keys_sorted_by_values(BASH_COLORS):
        c1 = color(c)
        c2 = color("white" if c != "white" else "black", bgcolor=c)
        print (c.ljust(10) +
               c1 + "colored text" + color() + "    " +
               c2 + "background" + color())
    print

    print header + "            " + "Attributes:             " + color()
    for c in _keys_sorted_by_values(BASH_ATTRIBUTES):
        c1 = color("red", attrs=c)
        c2 = color("white", attrs=c)
        print (c.ljust(13) +
               c1 + "red text" + color() + "     " +
               c2 + "white text" + color())
    print
    return


def color(color=None, bgcolor=None, attrs=None):
    if not is_bash():
        return ""

    ret = "\x1b[0"
    if attrs:
        for attr in attrs.lower().split():
            attr = attr.strip(",+|")
            if attr not in BASH_ATTRIBUTES:
                raise ValueError("Unknown color attribute: " + attr)
            ret += ";" + BASH_ATTRIBUTES[attr]

    if color:
        if color in BASH_COLORS:
            ret += ";" + BASH_COLORS[color]
        else:
            raise ValueError("Unknown color: " + color)

    if bgcolor:
        if bgcolor in BASH_BGCOLORS:
            ret += ";" + BASH_BGCOLORS[bgcolor]
        else:
            raise ValueError("Unknown background color: " + bgcolor)

    return ret + "m"


def is_bash():
    return os.environ.get("SHELL", "unknown").endswith("bash")


def _keys_sorted_by_values(adict):
    """Return list of the keys of @adict sorted by values."""
    return sorted(adict, key=adict.get)


if __name__ == "__main__":
    _main()
