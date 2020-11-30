import random
from itertools import product
from functools import reduce


def _generate_minesweeper(width, height, bombs):
    # init empty grid
    grid = [list(0 for _ in range(width)) for _ in range(height)]
    # select random positions for bombs (bomb spots may overlap, so we get AT MOST as many bombs as selected, but at least 1)
    bs = set([(random.randrange(height), random.randrange(width)) for _ in range(bombs)])
    for y in range(height):
        for x in range(width):
            ns = filter(lambda yx: 0 <= yx[1] < width and 0 <= yx[0] < height,  # filter out fields beyond the map boundries
                                  [(y + yoff, x + xoff)
                                    for (yoff, xoff) in product([-1, 0, 1], [-1, 0, 1])  # all neigbour coordinates
                                    if xoff != 0 or yoff != 0])  # remove offset (0,0) which is the cell itself
            bns = reduce(lambda acc, n: acc + (1 if n in bs else 0), ns, 0)  # count the bombs in the neighbourhood
            # if the position is one of the selected bomb spots, mark it as such.
            # If not, count the bombs in all neighbouring cells.
            grid[y][x] = -1 if (y, x) in bs else bns
    return grid


def _print_minesweeper(grid):
    emotes = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight"]
    s = ""
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            s += "||%s||" % (":bomb:" if grid[x][y] == -1 else ":%s:" % (emotes[grid[x][y]],),)
        s += "\n"
    s += ""
    return s


def minesweeper(width, height, bombs):
    print(_print_minesweeper(_generate_minesweeper(width, height, bombs)))


minesweeper(10, 10, 5)
