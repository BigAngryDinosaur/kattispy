import sys

read = lambda x: list(map(x, sys.stdin.readline().split()))

def main():
    num_cities = read(int)[0]
    for _ in range(num_cities):
        endpoints = read(int)[0]
        graph = { e:[] for e in range(endpoints) }
        for _ in range(read(int)[0]):
            s, d = read(int)
            graph[s].append(d)
            graph[d].append(s)

        visited = [False] * endpoints
        def dfs(node):
            visited[node] = True
            for d in graph[node]:
                if not visited[d]:
                    dfs(d)

        num_components = 0
        for s in range(endpoints):
            if not visited[s]:
                num_components += 1
                dfs(s)

        print(num_components-1)


if __name__ == "__main__":
    main()