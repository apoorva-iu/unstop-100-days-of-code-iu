# Unstop 100 Days of Code
# Day 21
# Possible words

def letterCombinations(digits):
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    result = []

    def backtrack(index, word):
        if index == len(digits):
            result.append(word)
            return

        for ch in mapping[digits[index]]:
            backtrack(index + 1, word + ch)

    if digits:
        backtrack(0, "")

    return result


if __name__ == '__main__':
    digits = input().strip()
    result = letterCombinations(digits)
    result.sort()
    print(' '.join(result))