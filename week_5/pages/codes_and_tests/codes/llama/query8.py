# def balanced_parentheses(s):
#     # Create a stack to keep track of open parentheses
#     stack = []
#     # Iterate over the characters in the input string
#     for c in s:
#         # If the character is an opening parenthesis, push it onto the stack
#         if c == '(':
#             stack.append(c)
#         # If the character is a closing parenthesis, and there are enough open parentheses on the stack, pop one off and check if the stack is balanced
#         elif c == ')':
#             if len(stack) > 0:
#                 # Pop the top item off the stack
#                 c = stack.pop()
#                 # If the character is a closing parenthesis and the previous character was an opening parenthesis, the parentheses are balanced
#                 if c == '(':
#                     return True
#             else:
#                 # If there are no open parentheses on the stack, or the previous character was not a closing parenthesis, the parentheses are unbalanced
#                 return
            

# def balanced_parentheses(s):
#     # Initialize an empty stack
#     stack = []

#     # Iterate over the characters in the input string
#     for c in s:
#         # If the character is a parenthesis, add it to the stack
#         if c == '(' or c == '{':
#             stack.append(c)
#         # If the character is a closing parenthesis, and there is a matching opening parenthesis on the stack, pop the stack and return True
#         elif c == '}' and stack:
#             return False

#         # Otherwise, just pass through the character
#         else:
#             pass

#     # If we reach this point, the parentheses are not balanced
#     return False


def balanced_parentheses(s):
    # Initialize two stacks, one for opening parentheses and another for closing parentheses
    open_stack = []
    close_stack = []
    
    # Iterate over the characters in the input string
    for c in s:
        # If the character is an opening parenthesis, add it to the open stack
        if c == '(' or c == '{':
            open_stack.append(c)
        
        # If the character is a closing parentheses, check if there are enough matching opening parentheses in the open stack
        elif c == ')':
            if len(open_stack) > 0:
                # Check that there are enough closing parentheses to match the opening ones
                if open_stack.pop() != c:
                    return False
        
        # If the character is a bracket, add it to the close stack
        elif c == '[' or c == ']':
            close_stack.append(c)
    
    # If there are no closing parentheses found in the input string, the parentheses are balanced
    return True
