def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    low = 0
    mid = 0
    high = len(input_list) - 1

    while mid <= high:
        if input_list[mid] == 0:
            input_list[low], input_list[mid] = input_list[mid], input_list[low]
            low += 1
            mid += 1
        elif input_list[mid] == 1:
            mid += 1
        else:  # input_list[mid] == 2
            input_list[mid], input_list[high] = input_list[high], input_list[mid]
            high -= 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Test case 1: Standard case with mixed 0s, 1s, and 2s
print("Test case 1: Standard case with mixed 0s, 1s, and 2s")
test_function([1, 2, 0, 1, 2, 0, 1, 2])  
# Expected Output: [0, 0, 1, 1, 1, 2, 2, 2]

# Test case 2: Edge case - Large array
print("Test case 2: Edge case - Large array")
large_array = [2, 0, 1] * 1000  # Creates a large array by repeating the pattern 1000 times
test_function(large_array)  
# Expected Output: [0, 0, 0, ..., 1, 1, 1, ..., 2, 2, 2]

# Test case 3: Edge case with an empty array
print("Test case 3: Edge case with an empty array")
test_function([])  
# Expected Output: []
