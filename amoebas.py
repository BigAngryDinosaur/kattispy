import sys

read = lambda x: list(map(x, sys.stdin.readline().split()))

def main():
    m, n = read(int)
    grid = [[''] * n for _ in range(m)]
    for r in range(m):
        line = sys.stdin.readline().rstrip()
        for c, val in enumerate(line):
            grid[r][c] = val

    amoebas = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == '#':
                stack = [(i, j)]
                while stack:
                    r, c = stack.pop()
                    if grid[r][c] == '#':
                        grid[r][c] = '$'
                    dollars = 0
                    for nr, nc in [(r,c+1),(r+1,c+1),(r+1,c),(r+1,c-1),(r,c-1),(r-1,c-1),(r-1,c),(r-1,c+1)]:
                        if 0 <= nr < m and 0 <= nc < n: 
                            if grid[nr][nc] == '#':
                                stack.append((nr, nc))
                            if grid[nr][nc] == '$':
                                dollars += 1
                    if dollars == 2:
                        amoebas += 1
                        stack = []
    print(amoebas)


if __name__ == "__main__":
    main()
