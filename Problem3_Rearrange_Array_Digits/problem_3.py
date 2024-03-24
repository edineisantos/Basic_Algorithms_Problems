def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Handling edge case: null value or empty list
    if not input_list:
        return [0, 0]

    quick_sort_descending(input_list, 0, len(input_list) - 1)
    first_number, second_number = "", ""
    for index in range(len(input_list)):
        if index % 2 == 0:
            first_number += str(input_list[index])
        else:
            second_number += str(input_list[index])
    
    # Ensure both numbers are integers, even if one part ends up being an 
    # empty string
    return [int(first_number) if first_number else 0, 
            int(second_number) if second_number else 0]

def quick_sort_descending(array, low, high):
    if low < high:
        partition_index = partition_for_descending_sort(array, low, high)
        quick_sort_descending(array, low, partition_index - 1)
        quick_sort_descending(array, partition_index + 1, high)

def partition_for_descending_sort(array, low, high):
    pivot_value = array[high]
    smaller_element_index = low - 1
    for current_index in range(low, high):
        if array[current_index] > pivot_value:
            smaller_element_index += 1
            array[smaller_element_index], array[current_index] = array[current_index], array[smaller_element_index]
    array[smaller_element_index + 1], array[high] = array[high], array[smaller_element_index + 1]
    return smaller_element_index + 1


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]

# Test case 1: Standard input
print("Test case 1: Standard input")
output = rearrange_digits([4, 6, 2, 5, 9, 8])
print(output)  
# Expected Output: [964, 852] or any other combination that results in the maximum sum

# Test case 2: Edge case - array with only one element
print("Test case 2: Edge case - array with only one element")
output = rearrange_digits([5])
print(output)  
# Expected Output: [5, 0]

# Test case 3: Edge case - input is None (null value)
print("Test case 3: Edge case - input is None (null value)")
output = rearrange_digits(None)
print(output)  
# Expected Output: [0, 0] or an appropriate handling of None input
