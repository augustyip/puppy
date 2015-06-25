#!/usr/bin/env python3

"""
Copyright (c) August Yip (http://august.hk/)
"""

import time
import curses

from curses import wrapper
import sys, traceback

from lib.core.data import config
from lib.source.yahoo import yahoo
from lib.source.tencent import tencent

def main() :

  try :
    stdscr.addstr(1,1, 'Loading...')
    stdscr.refresh()

    while True:

      stdscr.addstr(0, 0, 'puppy - version: 0.9.3.14159265')
      stdscr.addstr(1, 0, 'current data source: yahoo.finance, last refresh: ' + time.strftime('%H:%M:%S'))

      # quotes = yahoo.quotes()
      quotes = tencent.quotes()

      hsi_quote = quotes.pop(0)
      stdscr.addstr(2, 0, hsi_quote['Symbol'] + ': ' + hsi_quote['LastTradePriceOnly'] + ' - ' + hsi_quote['Change'] + ' - ' + hsi_quote['ChangeinPercent'] + ', DaysRange: ' + hsi_quote['DaysLow'] + ' - ' + hsi_quote['DaysHigh'])

      placeholder_str = '{symbol:10}{name:25}{price:6}{change:10}{percent:10}{dayslow:10}{dayshigh:30}'

      columns = {
        'symbol' : 'Symbol',
        'name' : 'Name',
        'price' : 'Price'.rjust(6),
        'change' : 'Change'.rjust(10),
        'percent' : 'Change%'.rjust(10),
        'dayslow' : 'DaysLow'.rjust(10),
        'dayshigh' : 'DaysHigh'.rjust(10),
      }

      row = 4

      stdscr.addstr(row, 0, placeholder_str.format(**columns), curses.A_REVERSE)

      for q in quotes:
        row += 1
        data = {
          'symbol' : q['Symbol'],
          'name' : q['Name'],
          'price' : q['LastTradePriceOnly'].rjust(6),
          'change' : q['Change'].rjust(10),
          'percent' : q['ChangeinPercent'].rjust(10),
          'dayslow' : q['DaysLow'].rjust(10),
          'dayshigh' : q['DaysHigh'].rjust(10),
        }

        stdscr.addstr(row, 0, placeholder_str.format(**data))
      stdscr.refresh()
      time.sleep(float(config['Yahoo']['refresh']))

  finally :
    curses.endwin()

if __name__ == '__main__':

  try :

    # Initialize curses
    stdscr=curses.initscr()

    # Turn off echoing of keys, and enter cbreak mode,
    # where no buffering is performed on keyboard input
    curses.noecho()
    curses.cbreak()
    
    # In keypad mode, escape sequences for special keys
    # (like the cursor keys) will be interpreted and
    # a special value like curses.KEY_LEFT will be returned
    stdscr.keypad(1)
    wrapper(main())

    # Enter the main loop
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
    # Print the exception
