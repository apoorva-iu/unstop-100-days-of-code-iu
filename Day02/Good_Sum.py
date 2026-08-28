# Unstop 100 Days of Code
# Day 2
# Good Sum

def good_sum(N, A):
    """
    Write your logic here.
    Parameters:
        N (int): The number of elements in the array
        A (list): The array of integers
    Returns:
        int: The final sum after performing the mentioned operation
    """
    stack = []
    total = 0

    for x in A:
        if x >= 0:
            stack.append(x)
            total += x
        else:
            need = -x
            removed = 0

            while stack and removed < need:
                val = stack.pop()
                removed += val
                total -= val

            stack.append(need)
            total += need

    return total


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])  # First input is the integer N
    A = list(map(int, data[1:]))  # Remaining input is the array of integers
    
    # Call user logic function and print the output
    result = good_sum(N, A)
    print(result)

if __name__ == "__main__":
    main()