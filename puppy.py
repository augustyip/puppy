import urllib.request
import urllib.parse

import json

import sys
import time

import socket

import curses

import traceback

def quotes() :

  endpoint = 'https://query.yahooapis.com/v1/public/yql?'

  params = {
    'q' : 'select * from yahoo.finance.quotes where symbol in ("0001.hk","0005.hk")',
    'format' : 'json',
    'env' : 'store://datatables.org/alltableswithkeys'
  }

  query_url = endpoint+ urllib.parse.urlencode(params)

  request = urllib.request.Request(query_url)
  request.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0')
  response = urllib.request.urlopen(request, timeout = 3)

  query_result = json.loads(response.read().decode("utf-8"))


  if len(query_result['query']['results']['quote']) > 0 :
    return query_result['query']['results']['quote']


def main(stdscr) :
  try:
    stdscr.refresh()
    # Your Code Stuff Here...
    stdscr.addstr(1,1, "Press Any Key to Exit...")
    # stdscr.getch()
    i = 0
    while True:
      quote = {}
      quote = quotes()

      title = '{0:25} {1} {2}'.format('Name', 'LastTradePriceOnly', 'ChangeinPercent')

      stdscr.addstr(3,1, title)

      y = 3
      for q in quote:
        y = y + 1
        data = '{0:25} {1} {2}'.format(q['Name'], q['LastTradePriceOnly'].rjust(10), q['ChangeinPercent'])
        stdscr.addstr(y,1, data)
      stdscr.refresh()
      time.sleep(3)
    
  finally:
    curses.endwin()


if __name__ == '__main__':
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
    main(stdscr)

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
