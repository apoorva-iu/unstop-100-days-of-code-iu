# Unstop 100 Days of Code
# Day 3
# Basketball_Game

def user_logic(ops):
    '''
    Write your logic here.
    Parameters:
        ops (list of str): List of operations as strings
    Returns:
        int: Computed result based on the problem statement
    '''
    stack=[]
    total=0
    for op in ops:
        if op=="C":
            removed=stack.pop()
            total-=removed
        elif op=="D":
            score=2*stack[-1]
            stack.append(score)
            total+=score
        elif op=="+":
            score=stack[-1]+stack[-2]
            stack.append(score)
            total+=score
        else:
            score=int(op)
            stack.append(score)
            total+=score
    return total
if __name__ == "__main__":
    n = int(input())  # Input for number of operations
    ops = input().split()
    
    # Call user logic function and print the output
    result = user_logic(ops)
    print(result)