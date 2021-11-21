import curses
from curses import wrapper
import time
import random
import json


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


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)


def wpm_test(stdscr, difficulty):
    sentence_file = open("sentences.json", "r")
    sentences_content = json.load(sentence_file)
    sentence_file.close()

    if difficulty.lower() == "e":
        target_text = random.choice(sentences_content["easy"])
    if difficulty.lower() == "m":
        target_text = random.choice(sentences_content["medium"])
    if difficulty.lower() == "h":
        target_text = random.choice(sentences_content["hard"])
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round(len(current_text) / (time_elapsed / 60) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()

        elif len(current_text) < len(target_text):
            current_text.append(key)


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
