# Unstop 100 Days of Code
# Day 10
# Box ab pattern

def follows_ab_pattern(s):
    """
    Write your logic here.
    Parameters:
        s (str): Input string representing the row of boxes
    Returns:
        str: "YES" if the sequence follows the "ab" pattern, otherwise "NO"
    """
    if "ba" in s:
        return "NO"
    return "YES"

def main():
    import sys
    input = sys.stdin.read
    s = input().strip()
    
    # Call user logic function and print the output
    result = follows_ab_pattern(s)
    print(result)

if __name__ == "__main__":
    main()