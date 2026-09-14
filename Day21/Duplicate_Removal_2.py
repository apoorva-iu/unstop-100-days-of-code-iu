# Unstop 100 Days of Code
# Day 21
# Duplicate Removal 2

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert_node(head, val):
    new_node = ListNode(val)
    if head[0] is None:
        head[0] = new_node
        return
    temp = head[0]
    while temp.next is not None:
        temp = temp.next
    temp.next = new_node

def print_list(node):
    if node is None:
        print("null")
        return
    while node is not None:
        print(node.val, end=" ")
        node = node.next
    print()

def delete_duplicates(head):
    """
    Write your logic here to delete duplicates from the linked list.
    Parameters:
        head (ListNode): Head of the linked list
    Returns:
        ListNode: Head of the linked list after removing duplicates
    """

    dummy = ListNode(0)
    dummy.next = head

    prev = dummy
    curr = head

    while curr:
        # Check if current value is duplicated
        if curr.next and curr.val == curr.next.val:

            # Remember the duplicate value
            duplicate = curr.val

            # Skip all nodes having this value
            while curr and curr.val == duplicate:
                curr = curr.next

            # Connect previous unique node to next different node
            prev.next = curr

        else:
            # Current node is unique
            prev = curr
            curr = curr.next

    return dummy.next

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])  # First input is the integer N
    head = [None]  # List to hold head reference

    for i in range(1, n+1):
        temp = int(data[i])
        insert_node(head, temp)  # Insert node

    res = delete_duplicates(head[0])  # Remove duplicates
    print_list(res)  # Print the resulting linked list

if __name__ == "__main__":
    main()
