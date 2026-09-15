# Unstop 100 Days of Code
# Day 22
# Start with End


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def build_linked_list(size, elements):
    if size == 0:
        return None
    head = Node(elements[0])
    tail = head
    for i in range(1, size):
        tail.next = Node(elements[i])
        tail = tail.next
    return head

def pair_sum(head):
    """
    Write your logic here.
    Parameters:
        head (Node): Head of the linked list
    Returns:
        int: Maximum sum of symmetric pairs
    """
  
    # Find the middle of the linked list
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half
    prev = None
    curr = slow

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # Find maximum symmetric pair sum
    first = head
    second = prev
    maximum = float('-inf')

    while second:
        maximum = max(maximum, first.val + second.val)
        first = first.next
        second = second.next

    return maximum

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    elements = list(map(int, data[1:n+1]))  # Next n inputs are the elements of the linked list
    
    head = build_linked_list(n, elements)
    
    # Call the user logic function and print the output
    result = pair_sum(head)
    print(result)

if __name__ == "__main__":
    main()
