# Unstop 100 Days of Code
# Day 15
# Minimum Addition

import sys


def minimum_addition(s: str) -> int:
    if not s:
        return 0

    # 1. Update the last character to 'c'
    s = s[:-1] + "c"
    n = len(s)

    if n <= 1:
        return 0

    # 2. Find longest palindromic PREFIX:
    # A prefix of s that matches a suffix of rev_s
    rev_s = s[::-1]
    combined = s + "#" + rev_s
    m = len(combined)

    lps = [0] * m
    for i in range(1, m):
        j = lps[i - 1]
        while j > 0 and combined[i] != combined[j]:
            j = lps[j - 1]
        if combined[i] == combined[j]:
            j += 1
        lps[i] = j

    longest_pal_prefix = lps[-1]

    # Minimum trees planted at the start
    return n - longest_pal_prefix


def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    print(minimum_addition(tokens[0]))


if __name__ == "__main__":
    main()