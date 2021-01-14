
import sys

read = lambda x: list(map(x, sys.stdin.readline().split()))

def main():
    cols, rows = read(int)
    grid = [[0] * cols for _ in range(rows)]
    for row in range(rows):
        vals = read(int)
        for col, h in enumerate(vals):
            grid[row][col] = h

    total_land = 0
    visited = [[False] * cols for _ in range(rows)]
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            stack = [(i, j)]
            can_grow = True
            area = 0
            if not visited[i][j]:
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    area += 1
                    for nr, nc in [(r,c+1), (r,c-1), (r-1,c), (r+1,c)]:
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == grid[r][c] and not visited[nr][nc]:
                                stack.append((nr, nc))
                                visited[nr][nc] = True
                            if grid[nr][nc] < grid[r][c]:
                                can_grow = False
            if can_grow:
                total_land += area

    print(total_land)

if __name__ == "__main__":
    main()