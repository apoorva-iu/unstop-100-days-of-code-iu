# Unstop 100 Days of Code
# Day 18
# Measurement of array

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    MOD = 10**9 + 7

    # 1. Sum of all original indices (0 to n - 1)
    # Every index from 0 to n - 1 is counted exactly once.
    original_indices_sum = (n * (n - 1) // 2) % MOD

    # 2. Count occurrences of each element
    # Constraints: 1 <= a_i <= 10^6, so a frequency array is O(N)
    freq = [0] * 1000001
    for i in range(1, n + 1):
        freq[int(input_data[i])] += 1

    # 3. Determine the last occurrence index of each unique value in the sorted array
    sorted_indices_sum = 0
    current_index = -1

    for count in freq:
        if count > 0:
            current_index += count  # Last 0-based index of this value in the sorted array
            sorted_indices_sum = (
                sorted_indices_sum + count * current_index
            ) % MOD

    total_measurement = (original_indices_sum + sorted_indices_sum) % MOD
    print(total_measurement)


if __name__ == "__main__":
    solve()