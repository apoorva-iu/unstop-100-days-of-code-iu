# Unstop 100 Days of Code
# Day 12
# FInd unique character from string

def determine_winner(N, smit_str, joy_str):

    smit_unique = len(set(smit_str))
    joy_unique = len(set(joy_str))

    if smit_unique > joy_unique:
        return "SMIT"
    elif joy_unique > smit_unique:
        return "JOY"
    else:
        return "TIE"


def main():
    import sys

    data = sys.stdin.read().split()

    N = int(data[0])

    if N == 0:
        print("TIE")
        return

    smit_str = data[1]
    joy_str = data[2]

    result = determine_winner(N, smit_str, joy_str)
    print(result)


if __name__ == "__main__":
    main()