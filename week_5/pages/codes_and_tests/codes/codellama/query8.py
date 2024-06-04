#Write a program that takes a string containing parentheses ((), {}, []) and determines if the parentheses are balanced

# def balanced_parentheses(string):
#     stack = []
#     for char in string:
#         if char == "(" or char == "[" or char == "{":
#             stack.append(char)
#         elif char == ")" or char == "]" or char == "}":
#             if len(stack) == 0:
#                 return False
#             top = stack.pop()
#             if (top == "(" and char != ")") or (top == "[" and char != "]") or (top == "{" and char != "}"):
#                 return False
#     if len(stack) != 0:
#         return False
#     else:
#         return True
    

def balanced_parentheses(s):
    stack = []
    for char in s:
        if char == "(" or char == "{" or char == "[":
            stack.append(char)
        elif char == ")" or char == "}" or char == "]":
            if len(stack) == 0:
                return False
            top = stack[-1]
            stack.pop()
            if (top == "(" and char != ")") or \
                    (top == "{" and char != "}") or \
                    (top == "[" and char != "]"):
                return False
    return len(stack) == 0