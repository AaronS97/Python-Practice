# Binary search algorithm implementation in Python

class Solution:

    arr = [-12, -9, -5, 0, 3, 7, 10, 15, 20]
    target = -9

    def binary_search(self, arr, target):
        # Set left and right pointers to first index and last index of the array, respectively
        l, r = 0, len(arr) - 1 

        # While the left pointer is less than or equal to the right pointer
        while l <= r:
            # Calculate the middle index
            mid = (l + r) // 2
            # If the target is found at the middle index, return the index
            if arr[mid] == target:
                return mid
            # If the target is less than the middle element, search in the left half
            elif arr[mid] > target:
                r = mid - 1
            # If the target is greater than the middle element, search in the right half
            else:
                l = mid + 1
        # If the target is not found, return -1
        return -1
    
if __name__ == "__main__":
    solution = Solution()
    result = solution.binary_search(solution.arr, solution.target)
    if result != -1:
        print(f"Target {solution.target} found at index: {result}")
    else:
        print(f"Target {solution.target} not found in the array.")