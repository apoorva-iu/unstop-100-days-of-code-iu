# Unstop 100 Days of Code
# Day 17
# AND triplets

def countTriplets(n, arr):
    MAX = 1 << 16

    pair = [0] * MAX

    for i in range(n):
        for j in range(n):
            value = arr[i] & arr[j]
            pair[value] += 1

    for bit in range(16):
        for mask in range(MAX):
            if mask & (1 << bit):
                pair[mask] += pair[mask ^ (1 << bit)]

    ans = 0

    for x in arr:
        allowed = (MAX - 1) ^ x
        ans += pair[allowed]

    return ans


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    arr = list(map(int, data[1:n+1]))

    result = countTriplets(n, arr)
    print(result)


if __name__ == "__main__":
    main()