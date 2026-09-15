# Unstop 100 Days of Code
# Day 22
# Remove the last occurence

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def remove_last_occurrences(head):
    """
    Write your logic here to remove the last occurrence of all elements in the linked list.
    
    Parameters:
        head (ListNode): The head of the linked list.
    Returns:
        ListNode: The head of the modified linked list.
    """
    
    freq = [0] * 10001
    last = [None] * 10001

    # Step 1: Count frequency and find last node
    current = head

    while current:
        freq[current.val] += 1
        last[current.val] = current
        current = current.next

    # Step 2: Remove nodes
    dummy = ListNode(0)
    dummy.next = head

    prev = dummy
    current = head

    while current:
        if freq[current.val] == 1 or last[current.val] is current:
            prev.next = current.next
        else:
            prev = current

        current = current.next

    return dummy.next


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    values = list(map(int, data[1:]))
    
    if n == 0:
        print("")
        return
    
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    
    modified_head = remove_last_occurrences(head)
    
    print_linked_list(modified_head)

if __name__ == "__main__":
    main()