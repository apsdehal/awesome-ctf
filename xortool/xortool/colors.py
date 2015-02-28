#!/usr/bin/env python
#-*- coding:utf-8 -*-

from libcolors import color

C_RESET = color()
C_FATAL = color("red")
C_WARN = color("yellow")

C_KEYLEN = color("green")
C_PROB = color("white", attrs="")
C_BEST_KEYLEN = color("green", attrs="bold")
C_BEST_PROB = color("white", attrs="bold")

C_DIV = color(attrs="bold")

C_KEY = color("red", attrs="bold")
C_BOLD = color(attrs="bold")
C_COUNT = color("yellow", attrs="bold")
