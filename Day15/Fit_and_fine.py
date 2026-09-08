# Unstop 100 Days of Code
# Day 15
# Fir and fine

def user_logic(fat, protein, vitamin):
    """
    Write your logic here.
    Parameters:
        fat (list): List of integers representing fat array
        protein (list): List of integers representing protein array
        vitamin (list): List of integers representing vitamin array
    Returns:
        tuple: Three integers representing the result based on the problem statement
    """

    fat_set = set(fat)
    protein_set = set(protein)
    vitamin_set = set(vitamin)

    fat_count = 0
    protein_count = 0
    vitamin_count = 0

    for x in fat:
        if x not in protein_set and x not in vitamin_set:
            fat_count += 1

    for x in protein:
        if x not in fat_set and x not in vitamin_set:
            protein_count += 1

    for x in vitamin:
        if x not in fat_set and x not in protein_set:
            vitamin_count += 1

    return fat_count, protein_count, vitamin_count




def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    fat = list(map(int, data[1:n+1]))  # Next N inputs are the fat array
    protein = list(map(int, data[n+1:2*n+1]))  # Next N inputs are the protein array
    vitamin = list(map(int, data[2*n+1:3*n+1]))  # Next N inputs are the vitamin array
    
    # Call user logic function and get the result
    result = user_logic(fat, protein, vitamin)
    
    # Print the result in the required format
    print(result[0], result[1], result[2])

if __name__ == "__main__":
    main()