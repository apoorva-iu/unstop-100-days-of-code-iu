# Unstop 100 Days of Code
# Day 18
# Cricket Match Score

import sys

def user_logic(n, runs):
    farthest = 0

    for i in range(n):

        if i > farthest:
            return False

        farthest = max(farthest, i + runs[i])

        if farthest >= n - 1:
            return True

    return True


if __name__ == "__main__":
    input = sys.stdin.read().split()
    n = int(input[0])
    runs = list(map(int, input[1:n+1]))
    
    result = user_logic(n, runs)
    print("true" if result else "false")