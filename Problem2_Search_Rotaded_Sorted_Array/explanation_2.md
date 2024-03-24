## Explanation for Problem 2: Search in a Rotated Sorted Array

The challenge of searching in a rotated sorted array necessitates an efficient approach that surpasses the linear time complexity. Given the sorted nature of the array before rotation, a modified binary search algorithm presents a viable solution, offering O(log n) time complexity. This problem's crux lies in identifying the pivot—the point of rotation—to discern the sorted segments of the array.

### Design Choices

#### Modified Binary Search
A conventional binary search algorithm assumes a fully sorted array, dividing the search space in half with each iteration. However, a rotated sorted array comprises two sorted subarrays. Thus, the algorithm is modified to first determine which half of the array contains the target value by comparing the array's middle element, start, and end. Depending on the comparison results, the search space is halved, either discarding the left or right segment.

- **Identifying Sorted Segments**: At any division point, at least one segment (left or right from the middle) is always sorted. We can easily check if a number falls within the sorted segment's range.
- **Adjusting Search Space**: If the target number lies within the sorted segment, the search continues within this segment. Otherwise, the search moves to the other segment, which might contain the pivot and part of the sorted array.

### Efficiency Analysis

#### Time Complexity
The time complexity of the modified binary search remains O(log n), where `n` is the number of elements in the array. Despite the array's rotation, the algorithm consistently eliminates half of the search space in each iteration, maintaining logarithmic time complexity.

#### Space Complexity
The space complexity is O(1), as the search operation is performed in place, requiring only a constant amount of space for variables used in calculating midpoints and storing indices.

### Conclusion

The solution to searching in a rotated sorted array efficiently leverages the principles of binary search with modifications to accommodate the array's rotated nature. By intelligently narrowing down the search space and capitalizing on the partially sorted property of the array, the algorithm achieves optimal time complexity with minimal space requirements. This approach underscores the importance of adapting classical algorithms to solve more complex problems effectively.
