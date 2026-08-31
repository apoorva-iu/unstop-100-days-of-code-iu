# Unstop 100 Days of Code
# Day 7
# Recent Submissions

# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_queue(n, arr):
    left = 0
    max_size = 0
    for right in range(n):
        # Kick out anyone from the front who is now 5000+ seconds old
        while arr[right] - arr[left] >= 5000:
            left += 1
        # Everyone between left and right is still "fresh"
        size = right - left + 1
        max_size = max(max_size, size)
    return max_size
 
 
n = int(input())
arr = list(map(int, input().split()))
print(max_queue(n, arr))