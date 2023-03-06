"""This program acts like minesweeper."""


def minesweeper():

    mine = [["-", "-", "-", "#", "#"],
            ["-", "#", "-", "-", "-"],
            ["-", "-", "#", "-", "-"],
            ["-", "#", "#", "-", "-"],
            ["-", "-", "-", "-", "-"]]

    count = 0
    for r in range(len(mine)):
        for c in range(len(mine)):  # This will iterate for every coordinate.

            if mine[r][c] == "#":  # Current
                continue

            else:
                if r == 0:  # this first statement and the ones later will make sure that for
                    pass    # outer rows and columns, there is no search out of range.
                elif mine[r-1][c] == "#":  # North position check.
                    count += 1

                if r == 0 or c == 0:
                    pass
                elif mine[r-1][c-1] == "#":  # Northwest position check.
                    count += 1

                if r == 0 or c == 4:
                    pass
                elif mine[r-1][c+1] == "#":  # Northeast position check.
                    count += 1

                if c == 0:
                    pass
                elif mine[r][c - 1] == "#":  # West position check.
                    count += 1

                if r == 4 or c == 0:
                    pass
                elif mine[r+1][c-1] == "#":  # Southwest position check.
                    count += 1

                if c == 4:
                    pass
                elif mine[r][c+1] == "#":  # East position check.
                    count += 1

                if r == 4 or c == 4:
                    pass
                elif mine[r+1][c+1] == "#":  # Southeast position check.
                    count += 1

                if r == 4:
                    pass
                elif mine[r + 1][c] == "#":  # South position check.
                    count += 1

            mine[r][c] = count
            count = 0
    for row in mine:
        print(row)


minesweeper()