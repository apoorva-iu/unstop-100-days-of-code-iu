# Unstop 100 Days of Code
# Day 9
# The 3 jumps

def min_cost(v):
    dp = [0] * len(v)

    dp[0] = 0

    for i in range(1, len(v)):

        # Jump from i-1
        dp[i] = dp[i - 1] + abs(v[i] - v[i - 1])

        # Jump from i-2
        if i >= 2:
            dp[i] = min(
                dp[i],
                dp[i - 2] + abs(v[i] - v[i - 2])
            )

        # Jump from i-3
        if i >= 3:
            dp[i] = min(
                dp[i],
                dp[i - 3] + abs(v[i] - v[i - 3])
            )

    return dp[-1]


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    v = list(map(int, data[1:]))

    result = min_cost(v)
    print(result)

if __name__ == "__main__":
    main()