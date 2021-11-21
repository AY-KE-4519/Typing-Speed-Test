from .display_text import display_text
import time
import random
import json


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
