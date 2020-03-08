# Curses based ui for musicderp's CatScan by Jellayy
# https://github.com/Jellayy

import time
import curses

menu = ['Start', 'Settings', 'Close']


def print_menu(window, selected_row_index):
    window.clear()
    h, w = window.getmaxyx()

    title = "CatScan v0.0 - musicderp & Jellayy"
    x = w//2 - len(title)//2
    window.addstr(0, x, title)

    for index, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + index
        if index == selected_row_index:
            window.attron(curses.color_pair(1))
            window.addstr(y, x, row)
            window.attroff(curses.color_pair(1))
        else:
            window.addstr(y, x, row)

    window.refresh()


# main menu
def mainui(window):
    # terminal customizations
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row_index = 0

    print_menu(window, current_row_index)

    while 1:
        key = window.getch()

        window.clear()

        if key == curses.KEY_UP and current_row_index > 0:
            current_row_index -= 1
        elif key == curses.KEY_DOWN and current_row_index < len(menu)-1:
            current_row_index += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row_index == 2:
                curses.endwin()
                quit()
            else:
                window.clear()
                window.addstr(0, 0, "You pressed {}".format(menu[current_row_index]))
                window.refresh()
                window.getch()

        print_menu(window, current_row_index)

        window.refresh()


# run mainui in curses wrapper
curses.wrapper(mainui)
