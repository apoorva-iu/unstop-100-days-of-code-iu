# Unstop 100 Days of Code
# Day 12
# Smallest Prime Multipler

import math

def compute_x(p, n):
    """
    Write your logic here.
    Parameters:
        p (int): First long long integer
        n (int): Second long long integer
    Returns:
        int: Computed result based on the problem statement
    """

    answer = (p * n) // math.gcd(p, n)

    return answer


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    p = int(data[0])
    n = int(data[1])

    result = compute_x(p, n)
    print(result)


if __name__ == "__main__":
    main()