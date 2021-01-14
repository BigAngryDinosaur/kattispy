import sys
import collections

read = lambda x: list(map(x, sys.stdin.readline().split()))

def main():
    c,p,h,s = read(int)
    graph = { x:[] for x in range(1,c+1) }
    in_degrees = { x:0 for x in range(1,c+1) }

    for _ in range(p):
        a,b = read(int)
        graph[a].append(b)
        graph[b].append(a)
        in_degrees[a] += 1
        in_degrees[b] += 1

    in_degrees[s] = 0
    sources = collections.deque([s])
    left = set()

    while sources:
        cn = sources.popleft()
        if cn in left:
            continue
        left.add(cn)
        for nei in graph[cn]:
            in_degrees[nei] -= 1
            if in_degrees[nei] <= len(graph[nei]) // 2:
                sources.append(nei)
    if h in left:
        print("leave")
    else:
        print("stay")


if __name__ == "__main__":
    main()