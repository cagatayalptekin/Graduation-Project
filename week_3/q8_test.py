#query_8="Write a program that takes a string containing parentheses ((), {}, []) and determines if the parentheses are balanced"



def balanced_parentheses_codellama(string):
    stack = []
    for char in string:
        if char == "(" or char == "[" or char == "{":
            stack.append(char)
        elif char == ")" or char == "]" or char == "}":
            if len(stack) == 0:
                return False
            top = stack.pop()
            if (top == "(" and char != ")") or (top == "[" and char != "]") or (top == "{" and char != "}"):
                return False
    if len(stack) != 0:
        return False
    else:
        return True
    

def is_balanced_llama(s):
    # Create a stack to keep track of open parentheses
    stack = []
    # Iterate through the string s and check if it's balanced
    for c in s:
        if c == '(' or c == '{':
            # Push the parenthesis onto the stack
            stack.append(c)
        elif c == '}':
            # Pop the matching parentheses from the stack
            stack.pop()
        elif c == ']':
            # If the stack is empty, then the parentheses are balanced
            return True
    # If the stack is not empty, then the parentheses are not balanced
    return False


def isBalanced_mistral(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
        elif c == '[':
            stack.append(c)
        elif c == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return False
    return len(stack) == 0