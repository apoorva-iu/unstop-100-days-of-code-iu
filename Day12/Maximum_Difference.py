# Unstop 100 Days of Code
# Day 12
# Maximum Difference

def user_logic(n, arr):
    """
    Write your logic here.
    Parameters:
        n (int): Size of the array
        arr (list): List of integers
    Returns:
        int: Computed result based on the problem statement
    """
    min_value = arr[0]
    max_diff = -1

    for i in range(1, len(arr)):
        diff = arr[i] - min_value

        if diff > 0:
            max_diff = max(max_diff, diff)

        min_value = min(min_value, arr[i])

    return max_diff

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx + N]))
        idx += N
        
        # Call user logic function and store the result
        result = user_logic(N, arr)
        results.append(result)
    
    # Print all results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()