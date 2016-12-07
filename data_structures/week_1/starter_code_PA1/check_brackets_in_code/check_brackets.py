# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    last_index = 1
    open_flag = False

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            open_flag = True
            last_index = i + 1
            item = Bracket(next, i+1)
            opening_brackets_stack.append(item)

        if next == ')' or next == ']' or next == '}':
            if len(opening_brackets_stack) == 0:
                last_index = i + 1
                break

            last = opening_brackets_stack.pop()
            if not last.Match(next):
                last_index = i + 1
                break

            last_index = i + 1

    if (len(opening_brackets_stack) == 0) and open_flag and (last_index % 2 == 0):
        print("Success")
    elif (len(text) != last_index) and (len(opening_brackets_stack) != 0):
        print(opening_brackets_stack[-1].position)
    else:
        print(last_index)


