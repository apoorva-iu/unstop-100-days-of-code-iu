# Unstop 100 Days of Code
# Day 8
# Counts_set_bits

def count_ones_in_binary(n):
    total=0
    for i in range(1,n+1):
        total+=bin(i).count('1')
    return total

if __name__ == "__main__":
    n = int(input())  # Read the integer N
    result = count_ones_in_binary(n)  # Call the user logic function
    print(result)  # Output the result