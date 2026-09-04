# Unstop 100 Days of Code
# Day 11
# Ravi Caught in string

def longest_palindromic_substring_length(n, s):
    """
    Write your logic here.
    Parameters:
        n (int): Length of the string
        s (str): The input string
    Returns:
        int: Length of the longest palindromic substring
    """
    dp = [[False] * n for _ in range(n)]
    max_len = 1

    # Single characters are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check substrings of length 2 to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

            if dp[i][j]:
                max_len = max(max_len, length)

    return max_len


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    s = data[1]  # Second input is the string S
    
    # Call user logic function and print the output
    result = longest_palindromic_substring_length(n, s)
    print(result)

if __name__ == "__main__":
    main()