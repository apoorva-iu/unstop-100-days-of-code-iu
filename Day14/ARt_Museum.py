# Unstop 100 Days of Code
# Day 14
# ARt Museum

def user_logic(n, positions):
    """
    Write your logic here.
    Parameters:
        n (int): Number of lakes
        positions (list of tuples): List of (xi, yi) positions of houses
    Returns:
        int: Number of different positions for the exhibition
    """
    x=[]
    y=[]
    for a,b in positions:
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    if n%2==1:
        x_choices=1
        y_choices=1
    else:
        x_choices=x[n//2]-x[n//2-1]+1
        y_choices=y[n//2]-y[n//2-1]+1
    return x_choices * y_choices

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    positions = []
    index = 1
    for i in range(n):
        x = int(data[index])
        y = int(data[index + 1])
        positions.append((x, y))
        index += 2
    
    # Call user logic function and print the output
    result = user_logic(n, positions)
    print(result)

if __name__ == "__main__":
    main()