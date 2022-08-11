import curses
import time


def draw(canvas):  # type: ignore
    row, column = (5, 20)
    canvas.addstr(row, column, 'Hello, World!')
    canvas.border()
    canvas.refresh()
    time.sleep(1)


if __name__ == '__main__':

    curses.update_lines_cols()
    curses.wrapper(draw)
