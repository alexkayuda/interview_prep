def isValid(s: str) -> bool:

    stack = []

    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        else:
            if len(stack) != 0:
                if char == ')' and stack[-1] != '(':
                    return False
                elif char == '}' and stack[-1] != '{':
                    return False
                elif char == ']' and stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            else:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    print(isValid("()"))
    print(isValid("({})"))
    print(isValid("(({}[]))"))
    print(isValid("(({}[])")) # False
    print(isValid("(({}[])))")) # False