# Unstop 100 Days of Code
# Day 5
# Backspace String Compare

def userLogic(bob, alice):

    def process_string(s):
        stack = []

        for ch in s:
            if ch == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)

    bob_final = process_string(bob)
    alice_final = process_string(alice)

    if bob_final == alice_final:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    bob = input().strip()
    alice = input().strip()

    result = userLogic(bob, alice)

    print(result)