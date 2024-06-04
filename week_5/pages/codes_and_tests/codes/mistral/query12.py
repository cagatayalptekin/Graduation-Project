def get_shortest_palindrome(s):
    # Find the substring that is equal to its reverse
    prefix = ""
    for i in range(len(s) - 1, -1, -1):
        start = i
        end = i + len(s)
        if s[i:] == s[::-1][:end - start]:
            prefix = s[i:]
            break
        
    # If no substring was found then the whole string needs to be reversed and prefixed
    if not prefix:
        return "a" + s[::-1]
    
    # Return the shortest palindrome as a result
    return prefix + s


# def get_shortest_palindrome(s):
#     # Find the substring of s which is equal to its reverse
#     prefix = ""
#     if s and s[0] == s[-1]:
#         return s

#     for i in range(len(s) - 1, -1, -1):
#         start = i
#         end = i + 1
#         while start > 0 and end < len(s) and s[start] != s[end]:
#             start -= 1
#             end += 1

#         if start == 0:
#             prefix = s[end:]
#             break

#     # Concatenate the prefix with reversed prefix to form the shortest palindrome
#     return prefix + str(prefix)[::-1]