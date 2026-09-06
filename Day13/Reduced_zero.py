# Unstop 100 Days of Code
# Day 13
# Reduced zero

def user_logic(n):
    # Write your logic here
    # Placeholder return
    if n % 2 == 0:
        return n // 2

    i = 3

    while i * i <= n:
        if n % i == 0:
            return 1 + (n - i) // 2

        i += 2

    return 1
    
n = int(input())
result = user_logic(n)
print(result)