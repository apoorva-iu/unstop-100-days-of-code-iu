# Unstop 100 Days of Code
# Day 10
# Parentheses Depth

# Python 3

def user_logic(n, s):
    """
    Write your logic here.
    Parameters:
        n (int): Length of the string S
        s (str): Valid parentheses string consisting of digits 0-9 and characters '+', '-', '*', '/', '(', ')'
    Returns:
        int: Maximum nesting depth of the string S
    """
    depth=0
    max_depth=0
    for ch in s:

        if ch=='(':
            depth+=1
            max_depth=max(depth,max_depth)
        if ch==')':
            depth-=1
    return max_depth


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    s = data[1]  # Second input is the string S
    
    # Call user logic function and print the output
    result = user_logic(n, s)
    print(result)


if __name__ == "__main__":
    main()