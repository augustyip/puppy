#!/usr/bin/env python3

"""
Copyright (c) August Yip (http://august.hk/)
"""

import time
import curses

from curses import wrapper
from datetime import datetime

import sys, traceback

from lib.core.config import config
from lib.source.yahoo import yahoo
from lib.source.tencent import tencent

def main() :
  try :

    # Initialize curses
    stdscr = curses.initscr()

    # Turn off echoing of keys, and enter cbreak mode,
    # where no buffering is performed on keyboard input
    curses.noecho()
    curses.cbreak()

    # In keypad mode, escape sequences for special keys
    # (like the cursor keys) will be interpreted andh
    # a special value like curses.KEY_LEFT will be returned
    stdscr.keypad(1)


    while True:
      stdscr.addstr(0, 0, 'puppy - version: 0.9.3.14159265')
      stdscr.addstr(1, 0, 'current data source: ' + config.config['Default']['source'] + ', last refresh: ' + time.strftime('%H:%M:%S'))
      # move to render function.
      
      stdscr.refresh()

    # Set everything back to normal
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
    # Terminate curses

  except :
    # In event of error, restore terminal to sane state.
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
    traceback.print_exc()
  finally :
    curses.endwin()

if __name__ == '__main__':
  main()
