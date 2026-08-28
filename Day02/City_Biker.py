def highestAltitude(n, arr):
    # Write your logic here
    # Placeholder return
    altitude = 0
    highest = 0

    for x in arr:
        altitude += x
        highest = max(highest, altitude)

    return highest

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = highestAltitude(n, arr)
    print(result)