# LeetCode Problem 1: Two Sum - Simple Brute Force
# Time Complexity: O(n^2) - This is the simplest approach but less efficient
# for large arrays compared to the O(n) hash map method.

def two_sum_simple(nums: list[int], target: int) -> list[int]:

    n = len(nums)

    # Outer loop iterates through each element's index 'i'
    for i in range(n):

        # Inner loop iterates through indices 'j' starting one position after 'i'
        # to ensure we don't use the same element twice (i != j)
        for j in range(i + 1, n):

            # Check if the pair sums to the target
            if nums[i] + nums[j] == target:
                # If the condition is met, return the indices immediately
                return [i, j]

    # If the loop finishes without finding a solution (though constraints guarantee one),
    # an empty list is returned.
    return []


# Example Test Case:
if __name__ == '__main__':
    nums_test = [15, 6, 9, 3]
    target_test = 12

    result = two_sum_simple(nums_test, target_test)

    print(f"Array: {nums_test}, Target: {target_test}")
    print(f"Indices found: {result}")
    # Expected Output: [1, 2] because nums[1] (6) + nums[2] (9) = 15