open_brackets = ['(', '{', '[']
close_brackets = [')', '}', ']']
def is_valid_parentheses(s):
    open_brackets_stack = []
    for i in s:
        if i in open_brackets:
            open_brackets_stack.append(i)
        else:
            if len(open_brackets_stack) == 0:
                return False
            idx = close_brackets.index(i)
            if open_brackets[idx] != open_brackets_stack.pop():
                return False

    if len(open_brackets_stack) == 0:
      return True
    return False

print(is_valid_parentheses('('))
print(is_valid_parentheses('()[]{}'))
print(is_valid_parentheses('(]'))
print(is_valid_parentheses('({[]})'))

