class Solution:
    # classic two pointer problem
    # O(n) time
    # sliding window
    # simple approach
    def search(self, nums, target):
        # handles edge cases
        left = 0
        # cleaner than before
        right = len(nums) - 1

        # works fine
        while left <= right:
            mid = left + (right - left) // 2

            # O(1) space
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Target is in the right half
                left = mid + 1
            else:
                # Target is in the left half
                right = mid - 1

        # Target not found
        return -1
