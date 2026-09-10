# Unstop 100 Days of Code
# Day 17
# Circular disc

def minTimeToType(word):
    """
    Write your logic here.
    Parameters:
        word (str): Input string
    Returns:
        int: Minimum number of seconds to print the string
    """
    s= sorted(word)

    current = 'a'
    time = 0

    for ch in s:
        clockwise = (ord(ch) - ord(current)) % 26
        counterclockwise = (ord(current) - ord(ch)) % 26

        time += min(clockwise, counterclockwise)
        time += 1

        current = ch

    return time

def main():
    import sys
    input = sys.stdin.read
    data = input().strip()
    
    # Call user logic function and print the output
    result = minTimeToType(data)
    print(result)

if __name__ == "__main__":
    main()