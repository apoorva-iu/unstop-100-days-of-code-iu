# Unstop 100 Days of Code
# Day 8
# Find class_id

import sys

# Function declaration
def peakIndexInMountainArray(A):
    # User logic here
    left=0
    right=len(arr)-1
    while left <right :
        mid=(left+right)//2
        if arr[mid]<arr[mid+1]:
            left=mid+1
        else:
            right=mid
    return left



if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(peakIndexInMountainArray(arr))