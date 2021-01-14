import sys

read = lambda x: list(map(x, sys.stdin.readline().split()))

def main():
    n = read(int)[0]
    nums = read(int)
    prev = 0
    gis = []
    for num in nums:
        if num > prev:
            gis.append(num)
            prev = num
    print(len(gis))
    print(*gis)

if __name__ == "__main__":
    main()