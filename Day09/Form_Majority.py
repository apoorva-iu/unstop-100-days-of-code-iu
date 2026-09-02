# Unstop 100 Days of Code
# Day 9
# Form Majority

# Enter your code here. Read input from STDIN. Print output to STDOUT

def majority(votes):
    votes.sort(reverse=True)

    total = sum(votes)
    selected = []
    current_sum = 0

    for vote in votes:
        selected.append(vote)
        current_sum += vote

        if current_sum > total - current_sum:
            break

    return selected


n = int(input())
votes = list(map(int, input().split()))

answer = majority(votes)

print(*answer)