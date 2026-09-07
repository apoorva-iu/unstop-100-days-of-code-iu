# Unstop 100 Days of Code
# Day 14
# Sum variation

def calculate_sum(nums):
    """
    Write your logic here.
    Parameters:
        nums (list): List of integers
    Returns:
        int: The sum obtained based on the problem statement
    """
    total=sum(nums)
    s=set(nums)
    missing=1
    while missing in s:
        missing +=1
    ascii_value=ord(str(missing)[0])
    return total+ascii_value

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    nums = list(map(int, data[1:]))  # Remaining input is the array of integers
    
    # Call the user logic function and print the output
    result = calculate_sum(nums)
    print(result)

if __name__ == "__main__":
    main()