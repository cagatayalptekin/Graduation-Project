def fib(n):
    # Base case 1
    if n <= 0:
        return n
    # Base case 2
    elif n == 1:
        return 0
    # Base case 3
    elif n == 2:
        return 1
    else:
        # Recursive call to get the previous two Fibonacci numbers
        a = fib(n-1)
        b = fib(n-2)
        # Calculate next Fibonacci number by adding previous two
        c = a + b
        # Return the calculated value
        return c
    

# def fib(n):
#     """Calculate n-th Fibonacci number using recursion"""
    
#     if n <= 0:
#         return n
    
#     # Base cases for first two numbers in the sequence
#     if n == 1 or n == 2:
#         return 1

#     # Calculate n-th Fibonacci number recursively
#     else:
#         return fib(n - 1) + fib(n - 2)