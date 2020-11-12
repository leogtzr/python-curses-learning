import curses
import time


def middle_screen_position(scr, text):
    h, w = scr.getmaxyx()
    x = (w//2) - (len(text)//2)
    y = h//2
    return y, x
    # h, w = src.getmaxyx()


def main(stdscr):
    options = ['A', 'B', 'C', 'D']
    option_index = 0
    curses.curs_set(0)

    while True:
        key = stdscr.getch()
        if key == curses.KEY_DOWN:
            stdscr.addstr(0, 0, "You pressed Down key!")
            option_index += 1
        elif key == curses.KEY_UP:
            stdscr.addstr(0, 0, "You pressed Up key!")
            option_index -= 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.addstr(0, 0, "Bye...")
            stdscr.refresh()
            time.sleep(1)
            break
            # curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)

            # text = 'Leonardo Gutierrez Ramirez'
            # x, y = middle_screen_position(stdscr, text)

            # stdscr.attron(curses.color_pair(1))

            # stdscr.addstr(x, y, text)
            # stdscr.attroff(curses.color_pair(1))

            # stdscr.refresh()
            # time.sleep(3)

            # stdscr = curses.initscr()

            # curses.noecho()

            # curses.curs_set(0)
            # stdscr.addstr(2, 0, 'Hello\nWorld')
            # stdscr.refresh()

            # time.sleep(5)

            # curses.curs_set(1)
            # curses.endwin()


curses.wrapper(main)
