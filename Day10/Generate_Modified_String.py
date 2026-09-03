# Unstop 100 Days of Code
# Day 10
# Generate Modified String

def modify_string(n, s):
    """
    Write your logic here.
    Parameters:
        n (int): Length of the alphanumeric string
        s (str): The alphanumeric string
    Returns:
        str: Modified string based on the problem statement
    """

    # Prime digits
    primes = {2, 3, 5, 7}

    # Store prime numbers found in the string
    prime_numbers = []

    for ch in s:
        if ch.isdigit():
            num = int(ch)

            if num in primes:
                prime_numbers.append(num)

    # Find unique number
    if prime_numbers:
        unique_number = sum(prime_numbers) // len(prime_numbers)
    else:
        unique_number = None

    # Build the answer
    result = ""

    for ch in s:
        if ch.isdigit():
            num = int(ch)

            if unique_number is not None:
                index = num % unique_number
            else:
                index = num

            result += chr(ord('a') + index)

        else:
            result += ch

    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    s = data[1]
    
    result = modify_string(n, s)
    print(result)

if __name__ == "__main__":
    main()