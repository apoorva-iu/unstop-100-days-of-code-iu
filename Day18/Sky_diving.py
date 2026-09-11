# Unstop 100 Days of Code
# Day 18
# Sky diving

import sys


def min_parachutes(k: int, n: int) -> int:
    # If there are no floors, 0 attempts are needed
    if n == 0:
        return 0
    # If there are floors to check but no parachutes, it cannot be determined
    if k == 0:
        return 0

    # dp[j] stores the maximum number of floors that can be checked
    # using j parachutes within the current count of attempts
    dp = [0] * (k + 1)
    attempts = 0

    while dp[k] < n:
        attempts += 1
        for parachutes in range(k, 0, -1):
            dp[parachutes] = dp[parachutes] + dp[parachutes - 1] + 1

    return attempts


def main():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return

    # Input format: N (floors), K (parachutes)
    n = int(input_data[0])
    k = int(input_data[1])

    result = min_parachutes(k, n)
    print(result)


if __name__ == "__main__":
    main()