import sys

def main():
    res = []
    while True:
        line = sys.stdin.readline().rstrip()
        if line == '':
            break
        m, n = list(map(int, line.split()))
        grid = [[''] * n for _ in range(m)]
        for i in range(m):
            line = sys.stdin.readline().rstrip()
            for j, val in enumerate(line):
                grid[i][j] = val

        def dfs(row, col):
            if grid[row][col] == '#':
                return
            grid[row][col] = '#'
            for nr, nc in [(row,col+1), (row+1,col+1), (row,col-1), (row-1,col)]:
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '-':
                    dfs(nr,nc)

        stars = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '-':
                    stars += 1
                    dfs(r, c)

        res.append(stars)

    for x, s in enumerate(res):
        print(f'Case {x+1}: {s}')

if __name__ == "__main__":
    main()