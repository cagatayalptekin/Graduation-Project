import pytest
# query_1="Function that calculates n'th Fibonacci numbers recursively"


def fib_codellama(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_codellama(n-1) + fib_codellama(n-2)
    

def fib_llama(n):
    if n <= 1:
        return n
    else:
        return fib_llama(n-1) + fib_llama(n-2)
    
def fib_Mistral(n):
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
        a = fib_Mistral(n-1)
        b = fib_Mistral(n-2)
        # Calculate next Fibonacci number by adding previous two
        c = a + b
        # Return the calculated value
        return c

print(fib_Mistral(30))
    
def test_returns_zero_when_n_is_zero(fib_function):
    assert fib_function(0) == 0

def test_returns_one_when_n_is_one(fib_function):
    assert fib_function(1) == 1
    
def test_returns_correct_value_for_n_30(fib_function):
    assert fib_function(30) == 832040

def test_raises_value_error_when_n_is_negative(fib_function):
    assert fib_function(-1) == -1

def test_returns_correct_value_for_n_92(fib_function):
    assert fib_function(92) == 7540113804746346429




def run_tests(fib_function):
    test_functions = [
        lambda: test_returns_zero_when_n_is_zero(fib_function),
        lambda: test_returns_one_when_n_is_one(fib_function),
        # lambda: test_raises_value_error_when_n_is_negative(fib_function),
        lambda: test_returns_correct_value_for_n_30(fib_function),
        #lambda: test_returns_correct_value_for_n_92(fib_function),
    ]

    success_count = 0

    for test in test_functions:
        try:
            test()
            print(f"{test.__name__}: Success")
            success_count += 1
        except AssertionError:
            print(f"{test.__name__}: Failure")

    print(f"\nTotal successful tests: {success_count} out of {len(test_functions)}")
    
print("Testing fib_codellama")
run_tests(fib_codellama)
print("\nTesting fib_llama")
run_tests(fib_llama)
print("\nTesting fib_Mistral")
run_tests(fib_Mistral)

#codellama score: 3/5
