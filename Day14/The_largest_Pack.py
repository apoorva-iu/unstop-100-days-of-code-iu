# Unstop 100 Days of Code
# Day 14
# The largest Pack

def find_largest_pack(N):
    """
    Write your logic here.
    Parameters:
        N (int): Number of marbles produced in a day
    Returns:
        int: Number of marbles in the largest pack that can be produced
    """
    power=1
    while power * 2 <=N:
        power=power * 2
    return power

def main():
    import sys
    input = sys.stdin.read
    
    # Read input
    data = input().strip()
    N = int(data)
    
    # Call user logic function and print the output
    result = find_largest_pack(N)
    print(result)

if __name__ == "__main__":
    main()