# Unstop 100 Days of Code
# Day 4
# Triangle Game

# Enter your code here. Read input from STDIN. Print output to STDOUT
def pascal_row(n):
    row = [1]

    for i in range(n):
        new_row = [1]

        for j in range(len(row) - 1):
            new_row.append(row[j] + row[j + 1])

        new_row.append(1)

        row = new_row

    return row


n = int(input())
print(*pascal_row(n))