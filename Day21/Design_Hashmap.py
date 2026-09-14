# Unstop 100 Days of Code
# Day 21
# Design Hashmap

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


def process_queries(queries):
    SIZE = 10007
    table = [None] * SIZE

    results = []

    for query in queries:

        # Type 1: Insert / Update
        if query[0] == 1:
            key = query[1]
            value = query[2]

            index = key % SIZE
            curr = table[index]

            # Key already exists → update value
            while curr:
                if curr.key == key:
                    curr.value = value
                    break
                curr = curr.next

            # Key does not exist → insert new node
            else:
                new_node = Node(key, value)
                new_node.next = table[index]
                table[index] = new_node

        # Type 2: Get
        elif query[0] == 2:
            key = query[1]

            index = key % SIZE
            curr = table[index]

            while curr:
                if curr.key == key:
                    results.append(curr.value)
                    break
                curr = curr.next
            else:
                results.append(-1)

        # Type 3: Delete
        elif query[0] == 3:
            key = query[1]

            index = key % SIZE
            curr = table[index]
            prev = None

            while curr:
                if curr.key == key:

                    if prev is None:
                        table[index] = curr.next
                    else:
                        prev.next = curr.next

                    break

                prev = curr
                curr = curr.next

    return results


import sys
input = sys.stdin.read
data = input().strip().split()

# Read number of queries
n = int(data[0])
index = 1

queries = []

for _ in range(n):
    query_type = int(data[index])
    if query_type == 1:
        key = int(data[index + 1])
        value = int(data[index + 2])
        queries.append((1, key, value))
        index += 3
    elif query_type == 2:
        key = int(data[index + 1])
        queries.append((2, key))
        index += 2
    elif query_type == 3:
        key = int(data[index + 1])
        queries.append((3, key))
        index += 2

# Call the user logic function
results = process_queries(queries)

# Print the results for type 2 queries
for result in results:
    print(result)