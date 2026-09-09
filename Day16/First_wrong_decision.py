# Unstop 100 Days of Code
# Day 16
# First wrong decision

def FirstWrongDecision(s):
    # User logic goes here
    for i in range(len(s)):
        if s[i] == 'W':
            return i

    return -1

if __name__ == '__main__':
    str = input()
    # Call the function FirstWrongDecision().
    print(FirstWrongDecision(str))