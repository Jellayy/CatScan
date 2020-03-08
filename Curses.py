# Curses based ui for musicderp's CatScan by Jellayy
# https://github.com/Jellayy

import time
import curses


# main menu
def mainui(window):
    # terminal customizations
    curses.curs_set(0)

    window.addstr(5, 5, "Whats poppin")
    window.refresh()
    time.sleep(3)


# run mainui in curses wrapper
curses.wrapper(mainui)
