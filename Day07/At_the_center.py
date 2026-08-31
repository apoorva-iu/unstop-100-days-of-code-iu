# Unstop 100 Days of Code
# Day 7
# At the center

# Enter your code here. Read input from STDIN. Print output to STDOUT
def find_closest_points(points, k):
    arr = []

    for x, y in points:
        distance = x * x + y * y
        arr.append((distance, x, y))

    arr.sort()

    result = []

    for i in range(k):
        result.append((arr[i][1], arr[i][2]))

    return result


def main():
    n = int(input())

    points = []

    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    k = int(input())

    result = find_closest_points(points, k)

    for x, y in result:
        print(x, y)


if __name__ == "__main__":
    main()