# Unstop 100 Days of Code
# Day 6
# Beer Purchase

def max_bottle_cost(n, x, costs):

    costs.sort()
    
    total_bottles = 0
    prefix = 0  
    

    for k in range(1, n + 1):
        prefix += costs[k - 1]  
        
        if prefix > x:

            break
            
        total_bottles += (x - prefix) // k + 1
    
    return total_bottles

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Number of shops
    x = int(data[1])  # Everyday budget
    costs = list(map(int, data[2:]))  # Costs of one bottle in each shop
    
    # Call user logic function and print the output
    result = max_bottle_cost(n, x, costs)
    print(result)

if __name__ == "__main__":
    main()