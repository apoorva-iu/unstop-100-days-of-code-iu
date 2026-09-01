# Unstop 100 Days of Code
# Day 8
# Golden value

def calculate_golden_value(arr, n):

    # Step 1: Prefix XOR
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] ^ arr[i]

    total = 0

    # Values can be up to 10^9
    # So check bits 0 to 30
    for bit in range(31):

        mask = 1 << bit

        even_zero = 0
        even_one = 0
        odd_zero = 0
        odd_one = 0

        # Count bits at even/odd prefix positions
        for i in range(n + 1):

            if prefix[i] & mask:

                if i % 2 == 0:
                    even_one += 1
                else:
                    odd_one += 1

            else:

                if i % 2 == 0:
                    even_zero += 1
                else:
                    odd_zero += 1

        # Even-length subarrays - odd-length subarrays
        total += (
            (even_zero - odd_zero)
            * (even_one - odd_one)
            * mask
        )

    return abs(total)


def main():
    import sys

    data = sys.stdin.read().split()

    n = int(data[0])
    arr = list(map(int, data[1:]))

    result = calculate_golden_value(arr, n)

    print(result)


if __name__ == "__main__":
    main()