def update_dictionary(dct, key, value):
    """
    - A function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, prints the original value, then updates its value.
    - Returns the updated dictionary.
    """
    if key in dct:
      print("Original Value: ",key, dct[key])

    dct[key]=value
    return "New Value: " + key + " " + str(value)

# Invoke the function "update_dictionary" using the following scenarios:
# Scenario 1:
print("Scenario 1")
print(update_dictionary({}, "name", "Alice"))

print("")

# Scenario 2:
print("Scenario 2")
print(update_dictionary({"age": 25}, "age", 26))
