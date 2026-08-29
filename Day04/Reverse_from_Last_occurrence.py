# Unstop 100 Days of Code
# Day 4
# Reverse from Last occurrence

def transform_string(s, ch):
    """
    Write your logic here.
    Parameters:
        s (str): Input string.
        ch (str): Character to be used in transformation.
    Returns:
        str: Transformed string.
    """
    index=s.rfind(ch)
    if index==-1:
        return s
    return s[:index]+s[index :][:: -1]


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    s = data[0]  # First input is the string s
    ch = data[1]  # Second input is the character ch
    
    # Call user logic function and print the output
    transformed_string = transform_string(s, ch)
    print(transformed_string)

if __name__ == "__main__":
    main()