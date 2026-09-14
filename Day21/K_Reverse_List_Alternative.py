# Unstop 100 Days of Code
# Day 21
# K Reverse List Alternative

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to swap nodes pairwise
def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head

    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = first.next

        first.next = second.next
        second.next = first
        prev.next = second

        prev = first

    return dummy.next


# Helper function to convert input string to linked list
def stringToListNode(input_str):

    if input_str == "[]":
        return None

    input_str = input_str[1:-1]
    input_str = input_str.replace(",", " ")

    values = list(map(int, input_str.split()))

    dummy = ListNode(0)
    ptr = dummy

    for val in values:
        ptr.next = ListNode(val)
        ptr = ptr.next

    return dummy.next


# Helper function to convert linked list to string
def listNodeToString(head):

    result = []

    while head:
        result.append(str(head.val))
        head = head.next

    return "[" + ", ".join(result) + "]"


# Main
input_str = input()

head = stringToListNode(input_str)

result = swapPairs(head)

print(listNodeToString(result))