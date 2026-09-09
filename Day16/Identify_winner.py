# Unstop 100 Days of Code
# Day 16
# Identify winner

def find_winner(arr):
    """
    Write your logic here.
    Parameters:
        arr (list): List of integers representing the numbers on the papers
    Returns:
        int: Number on the paper of the winner or 0 if there's no unique number
    """
    freq = {}

    # Count frequency
    for x in arr:
        freq[x] = freq.get(x, 0) + 1

    # Find first unique number
    for x in arr:
        if freq[x] == 1:
            return x

    return 0


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    arr = list(map(int, data[1:]))  # Remaining input is the array of integers
    
    # Call user logic function and print the output
    result = find_winner(arr)
    print(result)

if __name__ == "__main__":
    main()