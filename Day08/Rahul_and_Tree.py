# Unstop 100 Days of Code
# Day 8
# Rahul and Tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def userLogic(N, arr):

    arr.sort()

    def build(left, right):

        if left > right:
            return None

        # Choose the right-middle element
        mid = (left + right + 1) // 2

        root = Node(arr[mid])

        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)

        return root

    root = build(0, N - 1)

    def preorder(root):

        if root is None:
            return

        if root.left:
            left_value = root.left.val
        else:
            left_value = "."

        if root.right:
            right_value = root.right.val
        else:
            right_value = "."

        print(left_value, "<-", root.val, "->", right_value)

        preorder(root.left)
        preorder(root.right)

    preorder(root)


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    userLogic(N, arr)