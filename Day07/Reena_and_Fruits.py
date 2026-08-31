# Unstop 100 Days of Code
# Day 7
# Reena and Fruits

# Enter your code here. Read input from STDIN. Print output to STDOUT

def max_sum(nums):
  nums.sort()
  pairs=len(nums)//2
  total=0
  for i in range(pairs):
    total+=nums[2*i]
  return total

n=int(input())
nums=list(map(int,input().split()))
print(max_sum(nums))