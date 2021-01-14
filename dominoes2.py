import sys
import collections

read = lambda x: list(map(x, sys.stdin.readline().split()))

def main():
    num_test_cases = read(int)[0]
    for _ in range(num_test_cases):
        n, m, l = read(int)

        graph = { s:[] for s in range(1, n+1) }
        for _ in range(m):
            s, d = read(int)
            graph[s].append(d)
        
        visited = [False] * (n+1)
        dominoes = 0

        def dfs(node):
            nonlocal dominoes
            dominoes += 1
            visited[node] = True
            for des in graph[node]:
                if not visited[des]:
                    dfs(des)

        for _ in range(l):
            source = read(int)[0]
            if not visited[source]:
                dfs(source)
        
        print(dominoes)

if __name__ == "__main__":
    main()
