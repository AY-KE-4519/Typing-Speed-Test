def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nChoose the difficulty:")
    stdscr.addstr(3, 1, "1. Press E for easy")
    stdscr.addstr(4, 1, "2. Press M for medium")
    stdscr.addstr(5, 1, "3. Press H for hard")
    stdscr.refresh()
    key = stdscr.getkey()
    return key
