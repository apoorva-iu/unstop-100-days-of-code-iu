# Unstop 100 Days of Code
# Day 22
# special messages

def specialmsg(s, vocab):
    """
    Write your logic here.
    Parameters:
        s (str): Input string with acronyms
        vocab (list): List of key-value pairs, each a list of two strings [key, value]
    Returns:
        str: Modified string with acronyms replaced, or '?' if acronym not found
    """
    
    mapping = {}

    for key, value in vocab:
        mapping[key] = value

    result = []
    i = 0

    while i < len(s):

        if s[i] == '(':
            j = s.find(')', i)

            key = s[i + 1:j]

            if key in mapping:
                result.append(mapping[key])
            else:
                result.append('?')

            i = j + 1

        else:
            result.append(s[i])
            i += 1

    return ''.join(result)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    s = data[0]
    n = int(data[1])
    
    vocab = []

    for i in range(2, 2 + n):
        key, value = data[i].split()
        vocab.append([key, value])
    
    result = specialmsg(s, vocab)
    print(result)


if __name__ == "__main__":
    main()