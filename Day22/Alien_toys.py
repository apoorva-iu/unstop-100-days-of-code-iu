# Unstop 100 Days of Code
# Day 22
# Alien toys

def rearrange_blocks_to_form_name(S, P):
    n = len(S)
    m = len(P)

    if m > n:
        return 0, []

    p_count = [0] * 26
    window = [0] * 26

    # Count characters of P
    for ch in P:
        p_count[ord(ch) - ord('a')] += 1

    result = []

    # Create first window
    for i in range(m):
        window[ord(S[i]) - ord('a')] += 1

    # Check first window
    if window == p_count:
        result.append(1)

    # Slide the window
    for i in range(m, n):

        # Add new character
        window[ord(S[i]) - ord('a')] += 1

        # Remove old character
        window[ord(S[i - m]) - ord('a')] -= 1

        # Check current window
        if window == p_count:
            result.append(i - m + 2)

    return len(result), result


def main():
    import sys
    input = sys.stdin.read

    data = input().strip().split()

    S = data[0]
    P = data[1]

    num_groups, indices = rearrange_blocks_to_form_name(S, P)

    print(num_groups)

    if num_groups == 0:
        print("none")
    else:
        print(" ".join(map(str, indices)))


if __name__ == "__main__":
    main()