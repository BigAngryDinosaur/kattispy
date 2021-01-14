
import sys

read = lambda x: list(map(x, sys.stdin.readline().split()))

def main_graph():
    n, m = read(int)
    graph = { s:[] for s in range(1, n+1) }
    for _ in range(m):
        s, d = read(int)
        graph[s].append(d)
        graph[d].append(s)

    connected = set()
    visited = [False] * (n+1)
    visited[1] = True
    stack = [1]
    while stack:
        node = stack.pop()
        connected.add(node)
        for d in graph[node]:
            if not visited[d]:
                visited[d] = True
                stack.append(d)

    disconnected = set(range(1, n+1)).difference(connected)
    if not disconnected:
        print("Connected")
        return

    for d in disconnected:
        print(d)

class UF:

    def __init__(self, n):
        self.p = list(range(n+1))
        self.r = [0] * (n+1)

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.r[px] < self.r[py]:
            px, py = py, px
        if py == 1:
            px, py = py, px
        self.p[py] = px
        if self.r[px] == self.r[py]:
            self.r[px] += 1
        return True

def main_uf():
    n, m = read(int)
    uf = UF(n)
    for _ in range(m):
        s, d = read(int)
        uf.union(s, d)

    disconnected = set()
    for i in range(1, n+1):
        if uf.p[i] != 1:
            disconnected.add(i)

    if not disconnected:
        print("Connected")
    else:
        for i in disconnected:
            print(i)

if __name__ == "__main__":
    # main_graph()
    main_uf()
