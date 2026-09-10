# Unstop 100 Days of Code
# Day 17
# Find the posible words

import sys
from collections import Counter


def count_characters(words, chars):
    char_counts = Counter(chars)
    total_length = 0

    for word in words:
        word_counts = Counter(word)
        # If word_counts has no excess characters beyond char_counts, it can be formed
        if not (word_counts - char_counts):
            total_length += len(word)

    return total_length


def main():
    # Read all input tokens separated by any whitespace
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    words = tokens[1 : n + 1]
    chars = tokens[n + 1]

    print(count_characters(words, chars))


if __name__ == "__main__":
    main()