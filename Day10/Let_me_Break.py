# Unstop 100 Days of Code
# Day 10
# Let me Break

def check_if_can_break(s1, s2):
    if len(s1) != len(s2):
        return False

    s1 = sorted(s1)
    s2 = sorted(s2)

    s1_breaks = all(a >= b for a, b in zip(s1, s2))
    s2_breaks = all(b >= a for a, b in zip(s1, s2))

    return s1_breaks or s2_breaks


def main():
    import sys
    input = sys.stdin.read

    data = input().strip().split()

    s1 = data[0]
    s2 = data[1]

    result = check_if_can_break(s1, s2)

    if result:
        print("true")
    else:
        print("false")


if __name__ == "__main__":
    main()