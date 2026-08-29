# Unstop 100 Days of Code
# Day 5
# Repeating Box

# Enter your code here. Read input from STDIN. Print output to STDOUT

def find_repeated(arr):
    n = len(arr) // 2
    count = {}

    for x in arr:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1

        if count[x] == n:
            return x

    return -1


import sys

data = list(map(int, sys.stdin.read().split()))

total = data[0]
arr = data[1:]

print(find_repeated(arr))