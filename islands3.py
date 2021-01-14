
import sys

read = lambda x: list(map(x, sys.stdin.readline().split()))

def main():
    m,n = read(int)
    grid = [['']*n for _ in range(m)]
    for i in range(m):
        for j, c in enumerate(sys.stdin.readline().rstrip()):
            grid[i][j] = c

    islands = 0
    for a in range(m):
        for b in range(n):
            val = grid[a][b]
            if val == 'L':
                stack = [(a,b)]
                islands += 1
                while stack:
                    r,c = stack.pop()
                    for nr, nc in [(r,c+1), (r,c-1), (r+1,c), (r-1,c)]:
                        if 0 <= nr < m and 0 <= nc < n and (grid[nr][nc] == 'L' or grid[nr][nc] == 'C'):
                            stack.append((nr,nc))
                            grid[nr][nc] = '#'
    print(islands)

if __name__ == "__main__":
    main()