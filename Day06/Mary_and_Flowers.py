# Unstop 100 Days of Code
# Day 6
# Mary and Flowers

def find_flower_indices(n, t, arr):
    """
    Write your logic here.
    Parameters:
        n (int): Total types of flowers
        t (int): Total number of flowers needed
        arr (list): List of integers representing the flowers
    Returns:
        tuple: A tuple containing two integers representing the indices of the flowers
    """
    l=0
    r=n-1
    while l<r:
        total=arr[l]+arr[r]
        if total==t:
            return(l,r)
        elif total<t:
            l+=1
        else:
            r-=1

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    t = int(data[1])  # Second input is the integer t
    arr = list(map(int, data[2:]))  # Remaining input is the array of integers
    
    # Call user logic function and get the result
    result = find_flower_indices(n, t, arr)
    
    # Print the result
    print(result[0], result[1])

if __name__ == "__main__":
    main()