# Unstop 100 Days of Code
# Day 11
# Total cost of fuse bulb in the graph _hard

import sys
from collections import defaultdict, deque


def calculate_total_cost(k, n, m, graph):
    # If m == 0, no bulb can be divisible by 0; handles ZeroDivisionError
    if m == 0 or k == 0 or n == 0:
        return 0

    adj = defaultdict(list)
    for u, v in graph:
        adj[u].append(v)
        adj[v].append(u)

    visited = {0}
    queue = deque([0])
    count = 0

    while queue:
        curr = queue.popleft()
        if curr != 0 and curr % m == 0:
            count += 1
        for nxt in adj[curr]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)

    return count * k


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    k, n, m, len_graph = int(data[0]), int(data[1]), int(data[2]), int(data[3])

    graph = []
    idx = 4
    for _ in range(len_graph):
        graph.append([int(data[idx]), int(data[idx + 1])])
        idx += 2

    print(calculate_total_cost(k, n, m, graph))


if __name__ == "__main__":
    main()