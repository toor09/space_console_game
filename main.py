import asyncio
import curses
import time


async def blink(canvas, row, column, symbol='*'):  # type: ignore
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)


def draw(canvas):  # type: ignore
    row, column = (5, 20)
    canvas.border()
    curses.curs_set(False)
    coroutine_blink = blink(canvas, row, column)  # type: ignore
    while True:
        try:
            coroutine_blink.send(None)
            canvas.refresh()
            time.sleep(1)
        except StopIteration:
            break


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
