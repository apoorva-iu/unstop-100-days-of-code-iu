# Unstop 100 Days of Code
# Day 5
# Basic Encoding

import sys

def process_queries(q, queries):
    freq = {}
    for a, b in queries:
        freq[b] = freq.get(b, 0) + a  # accumulate counts for repeated B

    min_freq = min(freq.values())
    max_freq = max(freq.values())

    min_num = float('inf')
    max_num = float('-inf')
    for num, f in freq.items():
        if f == min_freq:                 # lowest frequency -> smallest number
            min_num = min(min_num, num)
        if f == max_freq:                 # highest frequency -> largest number
            max_num = max(max_num, num)

    print(abs(max_num - min_num))


def main():
    data = sys.stdin.read().split()
    idx = 0
    q = int(data[idx]); idx += 1

    queries = []
    for _ in range(q):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        queries.append((a, b))

    process_queries(q, queries)


if __name__ == "__main__":
    main()