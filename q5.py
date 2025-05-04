def check_divisibility(num, divisor):
    """
    - A function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if type(num) is int and type(divisor) is int:
      if num % divisor == 0:
         return True
      else:
         return False
    else:
      return "Error: Invalid number"
    return

# Invoke the function "check_divisibility" using the following scenarios:
# Scenario 1:
print("Scenario 1:")
print(check_divisibility(10, 2))

print("")

# Scenario 2:
print("Scenario 2:")
print(check_divisibility(7, 3))
