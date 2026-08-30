# Unstop 100 Days of Code
# Day 6
# Convert it

def modify_array(n, arr):
    """
    Modify the array based on the problem statement.
    Parameters:
        n (int): Size of the array
        arr (list): List of integers
    Returns:
        list: Modified array after applying the suggested changes
    """
    # User logic goes here
    max_value=0
    for i in range(len(arr)):
        max_value=max(max_value,arr[i])
        arr[i]=arr[i]+max_value
    return arr


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    arr = list(map(int, data[1:]))  # Remaining input is the array of integers
    
    # Call user logic function and get the modified array
    modified_arr = modify_array(n, arr)
    
    # Print the modified array
    print(" ".join(map(str, modified_arr)))


if __name__ == "__main__":
    main()