import sys

def main():
    for line in sys.stdin:
        n, *nums = list(map(int, line.rstrip().split()))
        taken = [0 for _ in range(1,n)]
        for i in range(1,n):
            idx = abs(nums[i-1] - nums[i])
            if 1 <= idx < n:
                taken[idx-1] += 1
            else:
                break
        if all(taken):
            print("Jolly")
        else:
            print("Not Jolly")

if __name__ == "__main__":
    main()