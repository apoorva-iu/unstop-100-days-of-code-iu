# Unstop 100 Days of Code
# Day 20
# Alice 's App

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def create_tree(data):
    if len(data) == 0 or data[0] == 'N':
        return None

    root = TreeNode(int(data[0]))
    queue = [root]
    i = 1

    while queue and i < len(data):
        current = queue.pop(0)

        if i < len(data) and data[i] != 'N':
            current.left = TreeNode(int(data[i]))
            queue.append(current.left)
        i += 1

        if i < len(data) and data[i] != 'N':
            current.right = TreeNode(int(data[i]))
            queue.append(current.right)
        i += 1

    return root

def left_view(root):
    """
    Write your logic here.
    Parameters:
        root (TreeNode): The root of the binary tree
    Returns:
        list: List of integers visible from the left side of the binary tree
    """
    
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        size = len(queue)

        for i in range(size):
            node = queue.pop(0)

            if i == 0:
                result.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    tree_nodes = data[1:n+1]
    
    root = create_tree(tree_nodes)
    
    result = left_view(root)
    
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
