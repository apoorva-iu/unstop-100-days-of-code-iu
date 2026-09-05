# Unstop 100 Days of Code
# Day 12
# Maths COmpetition

def minimumTime(N, K, A):
    if K == 0:
        return 0

    if N == 0:
        return -1

    if 0 in A:
        return 0

    low = 0
    high = min(A) * K

    while low < high:
        mid = (low + high) // 2

        total = 0

        for time in A:
            total += mid // time

            if total >= K:
                break

        if total >= K:
            high = mid
        else:
            low = mid + 1

    return low


N, K = map(int, input().split())

A = list(map(int, input().split()))

print(minimumTime(N, K, A))