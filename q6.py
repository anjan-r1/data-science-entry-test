def find_first_negative(lst):
    """
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    i = 0
    while i < len(lst):
      if lst[i] < 0:
        return lst[i]
      i += 1
    return "No negatives"

# Invoke the function "find_first_negative" using the following scenario:
# Scenario 1:
print("Scenario 1:")
print(find_first_negative([3, 5, -1, 7, -2, 8]))

print("")

# Scenario 2:
print("Scenario 2:")
print(find_first_negative([2, 10, 7, 0]))
