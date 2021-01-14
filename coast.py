import sys

read = lambda x: list(map(x, sys.stdin.readline().split()))

UNCHARTED_WATER = 0
UNCHARTED_LAND = 1
OCEAN = 2
LAND = 4

def main():
    m, n = read(int)
    grid = [[0]*n for _ in range(m)]
    for i in range(m):
        line = sys.stdin.readline().rstrip()
        for j in range(n):
            grid[i][j] = int(line[j])

    def dfs(rr, rc, f, t):
        if grid[rr][rc] == t:
            return
        grid[rr][rc] = t
        for mr, mc in [(rr,rc+1), (rr,rc-1), (rr+1,rc), (rr-1,rc)]:
            if 0 <= mr < m and 0 <= mc < n and grid[mr][mc] == f:
                dfs(mr, mc, f, t)

    for xc in range(n):
        if grid[0][xc] == UNCHARTED_WATER:
            dfs(0, xc, f=UNCHARTED_WATER, t=OCEAN)
        if grid[m-1][xc] == UNCHARTED_WATER:
            dfs(m-1, xc, f=UNCHARTED_WATER, t=OCEAN)

    for xr in range(m):
        if grid[xr][0] == UNCHARTED_WATER:
            dfs(xr, 0, f=UNCHARTED_WATER, t=OCEAN)
        if grid[xr][n-1] == UNCHARTED_WATER:
            dfs(xr, n-1, f=UNCHARTED_WATER, t=OCEAN)

    coast = 0
    for a in range(m):
        for b in range(n):
            col = grid[a][b]
            if col == UNCHARTED_LAND:
                stack = [(a,b)]
                grid[a][b] = LAND
                edges = 0
                while stack:
                    r,c = stack.pop()
                    for nr, nc in [(r,c+1), (r,c-1), (r+1,c), (r-1,c)]:
                        if 0 <= nr < m and 0 <= nc < n:  
                            if grid[nr][nc] == UNCHARTED_LAND:
                                grid[nr][nc] = LAND
                                stack.append((nr,nc))
                            elif grid[nr][nc] == OCEAN:
                                edges += 1
                        else:
                            edges += 1
                coast += edges
            
    print(coast)

if __name__ == "__main__":
    main()
