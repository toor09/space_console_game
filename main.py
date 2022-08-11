import asyncio
import curses
import time
from collections import namedtuple
from math import ceil
import random
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
        random.sample(frames, len(frames))
        for delay_frame, style_frame in frames:
            canvas.addstr(row, column, symbol, style_frame)
            await do_ticking(amount_of_ticks=delay_frame)   # type: ignore
            await asyncio.sleep(0)


def get_random_space_symbols(canvas, limit=100):
    settings = Settings()

    random_space_symbols = []
    for space_symbol in range(random.randint(0, limit)):
        max_y, max_x = curses.window.getmaxyx(canvas)
        random_row, random_column = random.randint(5, max_y - 5), random.randint(5, max_x - 5)
        random_space_symbols.append(
            blink(canvas, random_row, random_column, symbol=random.choice(settings.SPACE_SYMBOLS))
        )
    return random_space_symbols


def draw(canvas):  # type: ignore
    settings = Settings()
    canvas.border()
    curses.curs_set(False)
    coroutines = get_random_space_symbols(canvas, settings.SPACE_SYMBOLS_MAX_COUNT)
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
