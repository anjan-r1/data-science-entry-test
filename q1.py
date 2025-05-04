def swap(x, y):
    """
    The swap function would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Returns -1 if x and y is not numeric, and
    - prints the swapped values if both x and y are numeric.
    """
    if ((type(x) == int or type(x) == float) and (type(y) == int or type(y) == float)):
      [x,y] = [y,x]
      print(x,y)
    else:
      return -1

# Invoke the function "swap" using the below two scenarios:

# (Scenario 1)
swap("Apple", 10)

# (Scenario 2)
swap(-9, 17)
