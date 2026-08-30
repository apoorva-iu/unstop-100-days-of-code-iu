# Unstop 100 Days of Code
# Day 6
# Non-Overlapping Intervals

def erase_overlap_intervals(intervals):
    # User will implement this function
    intervals.sort(key=lambda x:x[1])
 

    removed = 0
    previous_end = intervals[0][1]



    for i in range (1, len(intervals)):
        start=intervals[i][0]
        end=intervals[i][1]
        if start<previous_end:
            removed+=1
        else:
            previous_end=end
    return removed 

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    intervals = []
    index = 2
    for _ in range(N):
        intervals.append([int(data[index]), int(data[index + 1])])
        index += 2
    result = erase_overlap_intervals(intervals)
    print(result)