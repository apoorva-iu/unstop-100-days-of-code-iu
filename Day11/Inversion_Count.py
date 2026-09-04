# Unstop 100 Days of Code
# Day 11
# Inversion Count

def user_logic(n, arr):
    """
    Write your logic here.
    Parameters:
        n (int): Size of the array
        arr (list): List of integers
    Returns:
        int: Computed result based on the problem statement
    """
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] ^ arr[j]) <= (arr[i] & arr[j]):
                count += 1

    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    arr = list(map(int, data[1:]))  # Remaining input is the array of integers
    
    # Call user logic function and print the output
    result = user_logic(n, arr)
    print(result)

if __name__ == "__main__":
    main()