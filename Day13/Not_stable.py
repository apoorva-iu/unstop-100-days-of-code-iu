# Unstop 100 Days of Code
# Day 13
# Not stable

def solve(arr, n):
    inc = sorted(arr)
    dec = sorted(arr, reverse=True)

    def valid(order):
        total = 0

        for x in order:
            total += x

            if total == 0:
                return False

        return True

    inc_valid = valid(inc)
    dec_valid = valid(dec)

    if not inc_valid and not dec_valid:
        print("IMPOSSIBLE")

    elif inc_valid and dec_valid:
        print("POSSIBLE")
        if inc[0] > dec[0]:
            print(*inc)
        else:
            print(*dec)

    elif inc_valid:
        print("POSSIBLE")
        print(*inc)

    else:
        print("POSSIBLE")
        print(*dec)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    solve(arr, n)