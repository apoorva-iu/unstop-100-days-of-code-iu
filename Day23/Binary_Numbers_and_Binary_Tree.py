# Unstop 100 Days of Code
# Day 23
# Binary Numbers and Binary Tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def make_tree(idx, n, arr):
    if idx >= n or arr[idx] == -1:
        return None

    root = TreeNode(arr[idx])
    root.left = make_tree(2 * idx + 1, n, arr)
    root.right = make_tree(2 * idx + 2, n, arr)

    return root


def user_logic(root):

    def dfs(node, num):

        if node is None:
            return 0

        num = num * 2 + node.val

        if node.left is None and node.right is None:
            return num

        return dfs(node.left, num) + dfs(node.right, num)

    return dfs(root, 0)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    arr = list(map(int, data[1:]))

    root = make_tree(0, n, arr)

    result = user_logic(root)
    print(result)


if __name__ == "__main__":
    main()