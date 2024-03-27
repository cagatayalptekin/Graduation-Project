#query_10="You are given a string s. You can convert s to a  palindrome by adding characters in front of it. Return the shortest palindrome you can find by performing this transformation."


def shortestPalindrome_codellama(s):
    # Write your code here
    if not s or len(s) == 0:
        return ""

    # reverse the string
    rev = s[::-1]
    palin_prefix = False

    for i in range(len(s)):
        if s[:i+1] == rev[i:]:
            palin_prefix = True

    return "a" * (len(s) - len(rev)) + s if not palin_prefix else s



def shortest_palindrome_llama(s):
    # Initialize an empty list to store the possible palindromes
    palindromes = []
    # Add characters in front of the given string to form palindromes
    for i in range(len(s)):
        palindromes.append(s[:i] + s[i:])
    # Return the shortest palindrome found
    return min(palindromes, key=len)


def shortest_palindrome_mistral(s):
    s = s.lower()
    n = len(s)
    for i in range(n):
        if i == 0 and n % 2 == 1:
            continue
        low = i - 1
        high = i + 1
        while low >= 0 and high < n and s[low] != s[high]:
            if high - low > 1:
                return s[:i] + 'x' + s[i:]
            low -= 1
            high += 1
    return s