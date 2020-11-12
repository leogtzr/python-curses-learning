import curses
import time


def middle_screen_position(scr, text):
    h, w = scr.getmaxyx()
    x = (w//2) - (len(text)//2)
    y = h//2
    return y, x
    # h, w = src.getmaxyx()


def main(stdscr):
    curses.curs_set(0)

    # stdscr.addstr(2, 3, 'Hello\nWorld')
    text = 'Leonardo Gutierrez Ramirez'
    x, y = middle_screen_position(stdscr, text)
    stdscr.addstr(x, y, text)
    stdscr.refresh()
    time.sleep(3)

# stdscr = curses.initscr()

# curses.noecho()

# curses.curs_set(0)
# stdscr.addstr(2, 0, 'Hello\nWorld')
# stdscr.refresh()

# time.sleep(5)

# curses.curs_set(1)
# curses.endwin()


curses.wrapper(main)
