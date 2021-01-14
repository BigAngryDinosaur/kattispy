import sys
import collections

read = lambda x: list(map(x, sys.stdin.readline().split()))

def main():
    n = read(int)[0]
    graph = collections.defaultdict(list)
    in_degrees = collections.defaultdict(int)
    for _ in range(n):
        f, deps = sys.stdin.readline().rstrip().split(':')
        deps = deps.split()
        in_degrees[f] = 0
        for dep in deps:
            graph[dep].append(f)
            in_degrees[f] += 1

    sources = collections.deque()
    for s,d in in_degrees.items(): 
        if d == 0:
            sources.append(s)
    res_order = []
    while sources:
        file = sources.popleft()
        res_order.append(file)
        for d in graph[file]:
            in_degrees[d] -= 1
            if in_degrees[d] == 0:
                sources.append(d)
    
    changed = sys.stdin.readline().rstrip()
    stack = [changed]
    res = set([changed])
    while stack:
        file = stack.pop()
        for d in graph[file]:
            if d not in res:
                stack.append(d)
                res.add(d)

    for file in res_order:
        if file in res:
            print(file)

if __name__ == "__main__":
    main()
