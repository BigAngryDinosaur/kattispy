import sys
import collections

read = lambda x: list(map(x, sys.stdin.readline().split()))

def main():
    n = read(int)[0]
    ballons = read(int)
    arrows = 0
    bmap = collections.defaultdict(int)
    for h in ballons:
        hp = h+1
        if bmap[hp] == 0:
            arrows += 1
        else:
            bmap[hp] -= 1
        bmap[h] += 1

    print(arrows)
    
if __name__ == "__main__":
    main()