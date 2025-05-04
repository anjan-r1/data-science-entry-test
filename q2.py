def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - A function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if (type(lst) == list):
      modified_list =[]
      for item in lst:
         if item == find_val:
            modified_list.append(replace_val)
         else:
            modified_list.append(item)
      return([modified_list])
    else:
      return("Not a list")

# Invoke the function "find_and_replace" for the below 2 scenarios:
# Scenario 1
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
# [[1, 5, 3, 4, 5, 5]]

# Scenario 2
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))
# [['orange', 'banana', 'orange']]

# Additional scenario:
# print(find_and_replace("apple", "apple", "orange"))
# -1
