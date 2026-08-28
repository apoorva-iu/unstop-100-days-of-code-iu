# Unstop 100 Days of Code
# Day 3
# Sum_Of_Different_Bits

def compareBits(a, b):
    m = len(a)
    n = len(b)

    windows = n - m + 1

    # Count 1s in the first window
    ones = b[:windows].count('1')

    total = 0

    for i in range(m):

        if a[i] == '0':
            total += ones
        else:
            total += windows - ones

        # Slide the window
        if i + windows < n:

            if b[i] == '1':
                ones -= 1

            if b[i + windows] == '1':
                ones += 1

    return total


if __name__ == '__main__':
    a = input().strip()
    b = input().strip()

    print(compareBits(a, b))