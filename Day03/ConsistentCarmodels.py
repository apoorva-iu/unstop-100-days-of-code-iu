# Unstop 100 Days of Code
# Day 3
# Consistent_Car_models

def count_consistent_cars(components, n, models):
    # User logic goes here
    allowed=set(components)
    count=0
    for model in models:
        valid=True
        for ch in model:
            if ch not in allowed:
                valid = False
                break
        if valid :
            count+=1

    return count  # Placeholder return value

if __name__ == '__main__':
 
    components = input().strip()
    n = int(input().strip())
    models = input().split()
    result = count_consistent_cars(components, n, models)
    print(result)