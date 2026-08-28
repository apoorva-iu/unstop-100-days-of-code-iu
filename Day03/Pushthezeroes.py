# Unstop 100 Days of Code
# Day 3
# Push_the_zeroes

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
arr=list(map(int,input().split()))

j=0
for i in range(n):
  if arr[i]!=0:
    arr[i],arr[j]=arr[j],arr[i]
    j+=1
print(*arr)