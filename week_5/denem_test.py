




import re

def get_function_name_and_params(func_str):
  """Extracts the function name and parameter list from a string representation of its definition.

  Args:
    func_str: A string containing the function definition.

  Returns:
    A tuple containing the extracted function name (or None if not found) and a list of parameter names.
  """
  lines = func_str.splitlines()
  if not lines:
    return None, None

  # Look for the first line that starts with 'def'
  for line in lines:
    if line.startswith('def'):
      # Extract function name and arguments
      match = re.match(r"^def\s+(.+?)\((.*?)\):", line)
    if match:
        function_name = match.group(1)
        return function_name, params
  return None, None


def get_function_name(func_str):
  """Extracts the function name from a string representation of its definition.

  Args:
      func_str: A string containing the function definition.

  Returns:
      The extracted function name or None if not found.
  """
  lines = func_str.splitlines()
  if not lines:
    return None

  # Look for the first line that starts with 'def'
  for line in lines:
    if line.startswith('def'):
      # Extract the function name from the line
      return line.split()[1].split('(')[0]
  return None

# Example usage
# code_string = """def fib_codellama(n,x,y):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fib_codellama(n-1) + fib_codellama(n-2)
# """








