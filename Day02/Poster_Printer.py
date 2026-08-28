# Unstop 100 Days of Code
# Day 2
# Poster Printer

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for _ in range(T):
    N = int(input())
    s = input()

    possible = True

    for group in s.split('W'):
        if group and ('B' not in group or 'R' not in group):
            possible = False
            break

    if possible:
        print("YES")
    else:
        print("NO")