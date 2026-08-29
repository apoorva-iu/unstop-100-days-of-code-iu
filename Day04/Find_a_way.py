# Unstop 100 Days of Code
# Day 4
# Find a way

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def user_logic(root):

    height = {}
    max_dia = 0

    # (node, visited)
    stack = [(root, False)]

    while stack:

        node, visited = stack.pop()

        if node is None:
            continue

        if visited == False:

            # Come back to this node after processing children
            stack.append((node, True))

            if node.right is not None:
                stack.append((node.right, False))

            if node.left is not None:
                stack.append((node.left, False))

        else:

            # Children are already processed
            left_height = height.get(node.left, 0)
            right_height = height.get(node.right, 0)

            # Diameter passing through this node
            max_dia = max(max_dia,
                           left_height + right_height)

            # Height of this node
            height[node] = max(left_height, right_height) + 1

    return max_dia


def construct_tree(i, nodes):

    n = len(nodes)

    # Create all nodes
    tree_nodes = []

    for j in range(n):
        tree_nodes.append(TreeNode(j + 1))

    # Connect left and right children
    for j in range(n):

        left = nodes[j][0]
        right = nodes[j][1]

        if left != -1:
            tree_nodes[j].left = tree_nodes[left - 1]

        if right != -1:
            tree_nodes[j].right = tree_nodes[right - 1]

    # Node 1 is the root
    return tree_nodes[0]


def main():

    import sys

    data = sys.stdin.read().strip().split()

    n = int(data[0])

    nodes = []

    index = 1

    for i in range(n):

        left = int(data[index])
        right = int(data[index + 1])

        nodes.append((left, right))

        index += 2

    root = construct_tree(0, nodes)

    result = user_logic(root)

    print(result)


if __name__ == "__main__":
    main()