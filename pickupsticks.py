import sys
import collections

read = lambda x: list(map(x, sys.stdin.readline().split()))


def topsort_dfs():

    UNVISITED = 0
    VISITING = 1
    VISITED = 2

    n,m = read(int)
    graph = collections.defaultdict(list)
    for _ in range(m):
        s,d = read(int)
        graph[s].append(d)
    
    visited = [UNVISITED] * (n+1)
    stick_order = collections.deque()
    def dfs(stick):
        visited[stick] = VISITING
        for nei in graph[stick]:
            if visited[nei] == UNVISITED:
                dfs(nei)
            elif visited[nei] == VISITING:
                print("IMPOSSIBLE")
                exit()
        visited[stick] = VISITED
        stick_order.appendleft(stick)

    for i in range(1,n+1):
        if visited[i] == UNVISITED:
            dfs(i)

    for si in stick_order:
        print(si)

def kahns():
    n,m = read(int)
    graph = { x:[] for x in range(1,n+1) }
    in_degrees = { x:0 for x in range(1,n+1) }
    for _ in range(m):
        s,d = read(int)
        graph[s].append(d)
        in_degrees[d] += 1
    
    sources = collections.deque()
    for s,d in in_degrees.items():
        if d == 0:
            sources.append(s)

    result = []    
    while sources:
        stick = sources.popleft()
        result.append(stick)
        for nei in graph[stick]:
            in_degrees[nei] -= 1
            if in_degrees[nei] == 0:
                sources.append(nei)
    
    if len(result) != n:
        print("IMPOSSIBLE")
    else:
        for si in result:
            print(si)
    
if __name__ == "__main__":
    # topsort_dfs()
    kahns()
