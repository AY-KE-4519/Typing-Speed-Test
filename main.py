import curses
from curses import wrapper
from funcs.start_screen import start_screen
from funcs.wpm_test import wpm_test


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    while True:
        difficulty = start_screen(stdscr)
        wpm_test(stdscr, difficulty)
        stdscr.addstr(
            2, 0, "You completed the text! Press any key to play again, or press Esc to exit")
        key = stdscr.getkey()

        if ord(key) == 27:
            break


wrapper(main)
