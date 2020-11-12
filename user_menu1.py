import curses
import time


def middle_screen_position(scr, text):
    h, w = scr.getmaxyx()
    x = (w//2) - (len(text)//2)
    y = h//2
    return y, x
    # h, w = src.getmaxyx()


menu = ['Home', 'Play', 'Scoreboard', 'Exit']
option_index = 0


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, option in enumerate(menu):
        x = w//2 - len(option)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            # Use attributes here ...
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, option)
            stdscr.attroff(curses.color_pair(1))
        else:
            # Use regular attributes here.
            stdscr.addstr(y, x, option)

    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row = 0

    print_menu(stdscr, current_row)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_DOWN and current_row < (len(menu)-1):
            stdscr.addstr(0, 0, "You pressed Down key!")
            current_row += 1
        elif key == curses.KEY_UP and current_row > 0:
            stdscr.addstr(0, 0, "You pressed Up key!")
            current_row -= 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.addstr(0, 0, f"Bye... {menu[current_row]}")
            stdscr.refresh()
            time.sleep(1)
            break

        stdscr.refresh()
        print_menu(stdscr, current_row)


curses.wrapper(main)
