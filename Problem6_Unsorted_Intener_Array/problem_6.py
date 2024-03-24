def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints or all(value is None for value in ints):
        return None

    min_val = max_val = ints[0]

    for num in ints[1:]: #Start from the second element
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return (min_val, max_val)

### Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Test Case 1: Empty array
print("Test Case 1: Empty array")
print(get_min_max([]))
# Expected Output: None

# Test Case 2: Array with None values
print("Test Case 2: Array with None values")
print(get_min_max([None, None, None]))
# Expected Output: None

# Test Case 3: Edge case - Array with negative integers
print("Test Case 3: Edge case - Array with negative integers")
l = [-3, -1, -9, -7, -4, -8, -6]
print(get_min_max(l))  
# Expected Output: (-9, -1)
