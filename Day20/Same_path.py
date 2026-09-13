# Unstop 100 Days of Code
# Day 20
# Same path

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def check(l1, l2):
    """
    Write your logic here.
    Parameters:
        l1 (Node): Head of the first linked list
        l2 (Node): Head of the second linked list
    Returns:
        int: 1 if the linked lists merge, otherwise 0
    """
    seen = set()

    # Store nodes of first linked list
    while l1:
        seen.add(l1)
        l1 = l1.next

    # Check nodes of second linked list
    while l2:
        if l2 in seen:
            return 1
        l2 = l2.next

    return 0

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Size of the first linked list
    m = int(data[1])  # Size of the second linked list
    
    map = {}
    
    # Create first linked list
    l1 = Node(0)
    temp = l1
    index = 2
    for i in range(n):
        t = int(data[index])
        index += 1
        if t in map:
            curr = map[t]
        else:
            curr = Node(t)
            map[t] = curr
        temp.next = curr
        temp = temp.next
    l1 = l1.next
    
    # Create second linked list
    l2 = Node(0)
    temp = l2
    for i in range(m):
        t = int(data[index])
        index += 1
        if t in map:
            curr = map[t]
        else:
            curr = Node(t)
            map[t] = curr
        temp.next = curr
        temp = temp.next
    l2 = l2.next
    
    # Call the user logic function
    result = check(l1, l2)
    print(result)

if __name__ == "__main__":
    main()