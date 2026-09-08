# Unstop 100 Days of Code
# Day 15
# Matching count

# Read total number of items
n = int(input())

# Read all items
items = []
for _ in range(n):
    items.append(input().split())

# Read the rule key and value
rule_key = input().strip()
rule_value = input().strip()

# Decide which index to check
if rule_key == "type":
    index = 0
elif rule_key == "color":
    index = 1
else:
    index = 2

# Count the matches
count = 0
for item in items:
    if item[index] == rule_value:
        count += 1

print(count)