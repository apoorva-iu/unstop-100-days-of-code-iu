# Unstop 100 Days of Code
# Day 23
# Binary Tree with Binary Nodes

import sys
import json
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def stringToTreeNode(input):
        input = input.strip()
        if not input:
            return None
        input = input[1:-1]
        if not input:
            return None

        parts = input.split(',')
        root = TreeNode(int(parts[0].strip()))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if index < len(parts):
                item = parts[index].strip()
                if item != "null":
                    node.left = TreeNode(int(item))
                    queue.append(node.left)
                index += 1
            if index < len(parts):
                item = parts[index].strip()
                if item != "null":
                    node.right = TreeNode(int(item))
                    queue.append(node.right)
                index += 1
        return root

    @staticmethod
    def treeNodeToString(root):
        if not root:
            return "[]"
        output = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                output.append("null")
                continue
            output.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        return "[" + ", ".join(output) + "]"


def pruneTree(root):
        # Function to prune the tree
    def prune(node):

        # If there is no node
        if node is None:
            return None

        # First prune the left subtree
        node.left = prune(node.left)

        # Then prune the right subtree
        node.right = prune(node.right)

        # If current node is 0 and has no children,
        # there is no 1 in this subtree, so delete it
        if node.val == 0 and node.left is None and node.right is None:
            return None

        # Otherwise keep the node
        return node

    # Start pruning from the root
    return prune(root)


if __name__ == '__main__':
    for line in sys.stdin:
        root = TreeNode.stringToTreeNode(line)
        result = pruneTree(root)
        print(TreeNode.treeNodeToString(result))
