# Unstop 100 Days of Code
# Day 16
# First palindrom string

import sys

def firstPalindrome(words):
    for word in words:
        left = 0
        right = len(word) - 1

        while left < right:
            if word[left] != word[right]:
                break

            left += 1
            right -= 1
        else:
            return word

    return ""


if __name__ == "__main__":
    data = sys.stdin.read().split()

    if not data:
        print("")
    else:
        n = int(data[0])
        words = data[1:n+1]

        print(firstPalindrome(words))