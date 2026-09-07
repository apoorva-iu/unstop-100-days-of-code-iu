# Unstop 100 Days of Code
# Day 14
# Robot Lap

def car_returns_to_origin(n, moves):
    """
    Write your logic here.
    Parameters:
        n (int): The size of the string moves
        moves (str): The string representing the moves
    Returns:
        str: "YES" if the car returns to origin, else "NO"
    """
    x=0
    y=0
    
    for move in moves:
        if move=='U':
            y+=1
        elif move=='D':
            y-=1
        elif move=='L':
            x+=1
        elif move=='R':
            x-=1
    if x==0 and y==0:
        return 'YES'
    else:
        return 'NO'


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    moves = data[1]  # Second input is the string moves
    
    # Call user logic function and print the output
    result = car_returns_to_origin(n, moves)
    print(result)

if __name__ == "__main__":
    main()