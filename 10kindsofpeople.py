import sys

read = lambda x: list(map(x, sys.stdin.readline().split()))

def main():
    m, n = read(int)
    grid = [[0]*n for _ in range(m)]
    for a in range(m):
        for b, v in enumerate(sys.stdin.readline().rstrip()):
            grid[a][b] = int(v)

    e,o = 2,3
    for i in range(m):
        for j in range(n):
            val = grid[i][j]
            if val == 1 or val == 0:
                stack = [(i,j)]
                while stack:
                    r,c = stack.pop()
                    for nr,nc in [(r,c+1),(r,c-1),(r+1,c),(r-1,c)]:
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == val:
                            stack.append((nr, nc))
                            if val % 2 == 0:
                                grid[nr][nc] = e
                            else:
                                grid[nr][nc] = o
                if val % 2 == 0:
                    e += 2
                else:
                    o += 2

    cases = read(int)[0]
    for _ in range(cases):
        r1, c1, r2, c2 = map(lambda x: x-1, read(int))
        if grid[r1][c1] == grid[r2][c2]:
            if grid[r1][c1] % 2 == 0:
                print("binary")
            else:
                print("decimal")
        else:
            print("neither")

if __name__ == "__main__":
    main()