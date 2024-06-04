#https://leetcode.com/problems/longest-valid-parentheses/description/

def longest_valid_parentheses(s):
    max_len = 0
    current_len = 0
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            stack.pop()
            current_len += 2
            
        if not stack:
            max_len = max(max_len, current_len)
    
    return max_len



# def longestValidParentheses(s):
#     max_len = 0
#     current_len = 0
#     stack = []
    
#     for i in range(len(s)):
#         if s[i] == '(':
#             stack.append(i)
#         elif s[i] == ')':
#             if not stack:
#                 max_len = max(max_len, current_len)
#                 current_len = 0
#             else:
#                 stack.pop()
#                 current_len = i - stack[-1]
    
#     return max(max_len, current_len)


# def longest_valid_parentheses(s):
#     max_len = 0
#     curr_len = 0
#     for i in range(len(s)):
#         if s[i] == '(':
#             curr_len += 1
#         else:
#             curr_len -= 1
#         if curr_len < 0:
#             curr_len = 0
#         max_len = max(max_len, curr_len)
#     return max_len