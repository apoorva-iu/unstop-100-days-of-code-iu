# Unstop 100 Days of Code
# Day 23
# Christmas and accessories

def find_possible_combinations(n, b, c, a):
    result = []

    def backtrack(path, b, c, a):
        # If we have selected N accessories
        if len(path) == n:
            result.append("".join(path))
            return

        # Select B
        if b > 0:
            path.append("B")
            backtrack(path, b - 1, c, a)
            path.pop()

        # Select C
        if c > 0:
            path.append("C")
            backtrack(path, b, c - 1, a)
            path.pop()

        # Select A
        if a > 0:
            path.append("A")
            backtrack(path, b, c, a - 1)
            path.pop()

    backtrack([], b, c, a)
    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    b = int(data[1])
    c = int(data[2])
    a = int(data[3])
    
    result = find_possible_combinations(n, b, c, a)
    
    for combination in result:
        print(combination)

if __name__ == "__main__":
    main()