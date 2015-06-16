
import data_source.yahoo


import time


import curses
import sys, traceback

from lib.core.data import config

def main() :

  try :
    # Your Code Stuff Here...
    stdscr.addstr(1,1, "Press Any Key to Exit...")
    # stdscr.getch()
    i = 0
    while True:
      quote = {}
      quote = data_source.yahoo.quotes()

      title = '{0:15} {1:10} {2}'.format('Name', 'Price'.rjust(10), 'Percent'.rjust(10))

      stdscr.addstr(3,1, title)

      y = 3
      for q in quote:
        y = y + 1
        data = '{0:15} {1:10} {2}'.format(q['Name'], q['LastTradePriceOnly'].rjust(10), q['ChangeinPercent'].rjust(10))
        stdscr.addstr(y,1, data)
      stdscr.refresh()
      time.sleep(float(config['Default']['refresh']))
    
  finally :
    curses.endwin()

if __name__ == '__main__':

  # data_source.yahoo.quotes()
  # sys.exit(0)

  # quotes();
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
    main()

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
