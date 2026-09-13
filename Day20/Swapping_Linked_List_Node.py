# Unstop 100 Days of Code
# Day 20
# Swapping Linked List Node

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapNodes(head, k):
    """
    Write your logic here.
    Parameters:
        head (ListNode): The head of the linked list
        k (int): The position of the nodes to be swapped
    Returns:
        ListNode: The head of the modified linked list
    """
        # 1. Find kth node from beginning
    left = head

    for i in range(k - 1):
        left = left.next

    # 2. Find kth node from end
    fast = head
    right = head

    for i in range(k):
        fast = fast.next

    # 3. Move both pointers together
    while fast:
        fast = fast.next
        right = right.next

    # 4. Swap their values
    left.val, right.val = right.val, left.val

    return head

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    values = list(map(int, data[1:n+1]))  # Next N inputs are the values of the linked list nodes
    k = int(data[n+1])  # Last input is the integer K

    # Create the linked list from the input values
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next

    head = dummy.next

    # Call the user logic function and get the modified linked list head
    modified_head = swapNodes(head, k)

    # Print the modified linked list
    result = []
    current = modified_head
    while current:
        result.append(current.val)
        current = current.next
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()