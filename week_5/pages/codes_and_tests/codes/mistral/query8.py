def balanced_parentheses(expression):
    opening_parentheses = '([{'
    closing_parentheses = ')]}'
    stack = []

    for char in expression:
        if char in opening_parentheses:
            stack.append(char)
        elif char in closing_parentheses:
            if not stack or stack.pop() != get_opening_parenthesis(char):
                return False

    return len(stack) == 0

def get_opening_parenthesis(closing_parenthesis):
    opening_parenthesis = {')': '(', ']': '[', '}': '{'}
    return opening_parenthesis[closing_parenthesis]



# def balanced_parentheses(string):
#     stack = []
#     opening_brackets = "([{"
#     closing_brackets = ")]}"

#     for char in string:
#         if char in opening_brackets:
#             stack.append(char)
#         elif char in closing_brackets:
#             if not stack or (stack.pop() if char != closing_brackets[::-1][0] else True):
#                 return False

#     # If we have popped all opening brackets, then the string is balanced
#     return len(stack) == 0


# def balanced_parentheses(parentheses):
#     stack = []
    
#     mapping = {")": "(", "}": "{", "]": "["]

#     for p in parentheses:
#         if p in mapping.values():
#             # If the character is an opening bracket, push it to the stack
#             stack.append(p)
#         else:
#             # If the character is a closing bracket and stack is empty or top element does not match with this closing bracket, then return False
#             if len(stack) == 0 or mapping[p] != stack[-1]:
#                 return False
            
#             # Otherwise pop from the stack
#             stack.pop()
    
#     # If all characters have been processed and stack is empty, then parentheses are balanced
#     return len(parentheses) == (len(mapping) + len(stack))