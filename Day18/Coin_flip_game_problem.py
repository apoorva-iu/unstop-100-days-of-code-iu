# Unstop 100 Days of Code
# Day 18
# Coin flip game problem

def find(m):
    count = 0

    for i in range(1, m + 1):
        if i * i <= m:
            count += 1

    return count


if __name__ == "__main__":
    m = int(input())
    count = find(m)
    print(count)