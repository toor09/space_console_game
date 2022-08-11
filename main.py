import asyncio
import curses
import time
from collections import namedtuple
from math import ceil

from settings import Settings


async def do_ticking(amount_of_ticks):   # type: ignore
    for _ in range(ceil(amount_of_ticks)):
        await asyncio.sleep(0)


async def blink(canvas, row, column, symbol="*"):  # type: ignore
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
    while True:
        for delay_frame, style_frame in frames:
            canvas.addstr(row, column, symbol, style_frame)
            await do_ticking(amount_of_ticks=delay_frame)   # type: ignore
            await asyncio.sleep(0)


def draw(canvas):  # type: ignore
    settings = Settings()
    row, column = (5, 20)
    canvas.border()
    curses.curs_set(False)
    coroutines = [blink(canvas, row, column, symbol="* "*5)]  # type: ignore
    while True:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
                canvas.refresh()
                time.sleep(settings.TIC_TIMEOUT)
            except StopIteration:
                coroutines.remove(coroutine)
            if len(coroutines) == 0:
                break


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
