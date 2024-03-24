def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 2:
        return number
    
    start, end = 1, number // 2
    while start <= end:
        mid = (start + end) // 2
        square = mid * mid
        
        if square == number:
            return mid
        elif square < number:
            start = mid + 1
            result = mid 
        else:
            end = mid - 1
            
    return result

# Test cases
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

# Test case 1: Standard input
print("Test case 1: Standard input")
print(sqrt(16))  # Expected Output: 4

# Test case 2: Edge case - unusually large value
print("Test case 2: Edge case - unusually large value")
print(sqrt(100000000))  # Expected Output: 10000

# Test case 3: Edge case - input is 0
print("Test case 3: Edge case - input is 0")
print(sqrt(0))  # Expected Output: 0