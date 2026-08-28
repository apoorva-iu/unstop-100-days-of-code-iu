# Unstop 100 Days of Code
# Day 2
# Pair of Subarrays

def calculate_pairs(n, arr):
    """
    Write your logic here.
    Parameters:
        n (int): The size of the array
        arr (list): List of integers representing the elements of the array
    Returns:
        int: The required number of pairs based on the problem statement
    """
    prefix = [0] * (n + 1)
        # Prefix sum
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    ans = 0
    freq = {}

    for start in range(n):

        # Store sums of subarrays ending before start
        for l in range(start):
            total = prefix[start] - prefix[l]
            freq[total] = freq.get(total, 0) + 1

        # Create subarrays starting at start
        for r in range(start, n):
            total = prefix[r + 1] - prefix[start]

            # How many left subarrays have same sum?
            ans += freq.get(total, 0)

    return ans

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    n = int(data[0])  # The first line of input, integer N
    arr = list(map(int, data[1:n+1]))  # The second line of input, N space-separated integers
    result = calculate_pairs(n, arr)
    print(result)

if __name__ == "__main__":
    main()