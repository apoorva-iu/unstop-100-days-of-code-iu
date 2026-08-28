def determine_color(s):
    """
    Write your logic here to determine the color based on the string s.
    Parameters:
        s (str): Input string representing a position.
    Returns:
        str: "Black" or "White" based on the problem statement.
    """
    col=ord(s[0].lower())-ord('a') + 1
    row=int(s[1])
    total=col+row
    if total % 2==0:
        return "Black"
    else:
        return "White"
def main():
    import sys
    input = sys.stdin.read
    s = input().strip()  # Read the input string
    
    # Call the user logic function and print the output
    result = determine_color(s)
    print(result)

if __name__ == "__main__":
    main()