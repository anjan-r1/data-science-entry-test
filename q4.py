def string_reverse(s):
    """
    Task 1
    - A function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    print("Original String:",s)
    r=""
    for i in range(len(s)-1,-1, -1):
      r = r + s[i]
    return "Reversed String: " + r


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# Scenario 1:
print("Scenario 1")
print(string_reverse("Hello World"))

print("")

# Scenario 2:
print("Scenario 2")
print(string_reverse("Python"))
