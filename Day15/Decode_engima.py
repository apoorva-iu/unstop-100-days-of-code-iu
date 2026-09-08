# Unstop 100 Days of Code
# Day 15
# Decode engima

def interpret(s):
    """
    Write your logic here.
    Parameters:
        s (str): Input string
    Returns:
        str: Interpreted command string
    """
    s = s.replace("[sps]", "ships ")
    s = s.replace("[]", "the ")
    s = s.replace("S", "send ")
    return s.strip()

def main():
    import sys
    input = sys.stdin.read
    
    # Read input string
    s = input().strip()
    
    # Call user logic function and print the output
    result = interpret(s)
    print(result)

if __name__ == "__main__":
    main()