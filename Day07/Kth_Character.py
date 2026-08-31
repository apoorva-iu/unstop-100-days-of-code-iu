# Unstop 100 Days of Code
# Day 7
# Kth Character

# Enter your code here. Read input from STDIN. Print output to STDOUT

def find_kth_character(n, k, s):
    return s[n - k]


def main():
    n, k = map(int, input().split())
    s = input().strip()

    result = find_kth_character(n, k, s)

    print(result)


if __name__ == "__main__":
    main()