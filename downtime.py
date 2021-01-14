import sys
import collections

read = lambda x: list(map(x, sys.stdin.readline().split()))

def main():
    n,k = read(int)
    max_requests = 0
    queue = collections.deque()

    for _ in range(n):
        request = read(int)[0]
        while queue and request - queue[0] >= 1000:
            queue.popleft()
        queue.append(request)
        max_requests = max(max_requests, len(queue))
    
    servers = max_requests // k
    if max_requests % k == 0:
        print(servers)
    else:
        print(servers+1)

    
if __name__ == "__main__":
    main()