# bracket_checker.py

from atds import Stack


def is_valid(expr):
    stack = Stack()

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for ch in expr:
        if ch in "([{":
            stack.push(ch)

        elif ch in ")]}":
            if stack.is_empty():
                return False

            top = stack.pop()

            if top != pairs[ch]:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    test = input("Enter expression: ")
    if is_valid(test):
        print("Valid expression.")
    else:
        print("Invalid expression.")