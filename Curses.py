# Curses based ui for musicderp's CatScan by Jellayy
# https://github.com/Jellayy

import time
import curses

# initialize window object
window = curses.initscr()

# terminal window configurations
curses.noecho()
curses.cbreak()
curses.curs_set(0)

# display string
window.addstr(5, 5, "What's Poppin")
window.refresh()
time.sleep(3)

# close window and reset terminal customizations
curses.curs_set(1)
curses.echo()
curses.nocbreak()
curses.endwin()
