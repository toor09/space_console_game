import curses
import time
from collections import namedtuple


def draw(canvas):  # type: ignore
    row, column = (5, 20)
    canvas.border()
    curses.curs_set(False)
    star = "*"
    StarFrame = namedtuple("StarFrame", "delay style")
    dim_star_frame = StarFrame(delay=2, style=curses.A_DIM)
    bold_star_frame = StarFrame(delay=0.3, style=curses.A_BOLD)
    default_star_frame = StarFrame(delay=0.3, style=0)
    frames = (
        dim_star_frame,
        default_star_frame,
        bold_star_frame,
        default_star_frame,
    )
    for delay_frame, style_frame in frames:
        canvas.addstr(row, column, star, style_frame)
        time.sleep(delay_frame)
        canvas.refresh()


if __name__ == '__main__':
    while True:
        curses.update_lines_cols()
        curses.wrapper(draw)
