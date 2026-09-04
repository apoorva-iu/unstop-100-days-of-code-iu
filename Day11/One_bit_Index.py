# Unstop 100 Days of Code
# Day 11
# One bit Index

def count_good_indices(n, arr):
    """
    Write your logic here.
    Parameters:
        n (int): The size of the array
        arr (list): List of integers representing the array
    Returns:
        int: Number of good indices in the array
    """
    total = 0
    count = 0

    for i in range(n):
        total += arr[i]

        if total > 0 and (total & (total - 1)) == 0:
            count += 1

    return count


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    arr = list(map(int, data[1:n+1]))  # Next N inputs are the elements of the array
    
    # Call user logic function and print the output
    result = count_good_indices(n, arr)
    print(result)


if __name__ == "__main__":
    main()