# Unstop 100 Days of Code
# Day 13
# diagonal sum

def diagonal_sum(matrix, n):
    answer = 2 * n

    if n % 2 == 1:
        answer -= 1

    return answer


if __name__ == '__main__':
    n = int(input())
    result = diagonal_sum([], n)
    print(result)