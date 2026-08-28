# Unstop 100 Days of Code
# Day 1
# Problem 3

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from collections import Counter

def kth_unique(strings, k):
    count = Counter(strings)   # counts how many times each string appears
    
    # Build a list of only the strings that appear EXACTLY once,
    # in the order they first appeared
    unique_list = [s for s in strings if count[s] == 1]
    
    if k <= len(unique_list):
        return unique_list[k - 1]   # k-1 because lists start at index 0
    else:
        return -1

def main():
    data = sys.stdin.read().split()
    idx = 0
    
    n = int(data[idx]); idx += 1
    
    strings = []
    for _ in range(n):
        strings.append(data[idx]); idx += 1
    
    k = int(data[idx]); idx += 1
    
    result = kth_unique(strings, k)
    print(result)

if __name__ == "__main__":
    main()