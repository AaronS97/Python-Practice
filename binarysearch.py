class Solution:
    arr = [-23, -12, -8, -3, 0, 1, 5, 6, 9, 11, 18]
    target = 11

    def binarysearch(self, arr, target):
        # Set right and left indexes 
        l, r = 0, len(arr) - 1
        # While left pointer is less than right pointer
        while l <= r:
            # Calculate midpoint index
            m = l + (r - l)//2
            # If current index equals target, return index
            if arr[m] == target:
                return m
            # If current index is less than target, check right half by moving left pointer to 1 index beyond midpoint index 
            elif arr[m] < target:
                l = m + 1
            # If current index is greater than target, check right half by moving right pointer to 1 index behind midpoint index
            elif arr[m] > target:
                r = m - 1
        # If target is not found in the array, return -1
        return -1

if __name__ == "__main__":
    solution = Solution()
    result = solution.binarysearch(solution.arr, solution.target)
    if result != -1:
        print(f"Target {solution.target} found at index: {result}")
    else: 
        print(f"Target {solution.target} not found in array")