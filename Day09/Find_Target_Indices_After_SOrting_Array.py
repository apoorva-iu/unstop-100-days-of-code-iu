# Unstop 100 Days of Code
# Day 9
# Find Target Indices After SOrting Array

# Enter your code here. Read input from STDIN. Print output to STDOUT

def find_indexes(N, A, K):
    A.sort()

    indexes = []

    for i in range(N):
        if A[i] == K:
            indexes.append(i)

    print(len(indexes))
    print(*indexes)


N = int(input())
A = list(map(int, input().split()))
K = int(input())

find_indexes(N, A, K)