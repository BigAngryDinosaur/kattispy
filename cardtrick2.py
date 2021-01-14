import sys
import collections

read = lambda x: list(map(x, sys.stdin.readline().split()))

def main():
    cases = read(int)[0]
    for _ in range(cases):
        n = read(int)[0]
        queue = collections.deque([n])
        for i in range(n-1, 0, -1):
            queue.appendleft(i)
            for j in range(i):
                queue.appendleft(queue.pop())
        print(" ".join(map(str, queue)))

if __name__ == "__main__":
    main()
