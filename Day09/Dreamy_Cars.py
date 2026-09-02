# Unstop 100 Days of Code
# Day 9
# Dreamy Cars

def calculate_f_score(features, N):
    answer = 0

    for i in range(N):
        count = (i + 1) * (N - i)

        if count % 2 == 1:
            answer ^= features[i]

    return answer


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])
    features = list(map(int, data[1:]))
    
    result = calculate_f_score(features, N)
    print(result)


if __name__ == "__main__":
    main()