class Solution:
    # simple dp, nothing fancy
    def findLengthOfLCIS(self, nums):
        # Base case for empty array is not needed due to constraints (length >= 1)
        # For a single element array, max_len starts at 1 and loop doesn't run, correctly returns 1.

        max_len = 1
        current_len = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_len += 1
            else:
                current_len = 1 # Reset if not strictly increasing

            max_len = max(max_len, current_len)

        return max_len
