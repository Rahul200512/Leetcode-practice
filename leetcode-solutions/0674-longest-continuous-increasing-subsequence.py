class Solution:
    # simple dp, nothing fancy
    # cleaner than before
    # O(n) time
    def findLengthOfLCIS(self, nums):
        # Base case for empty array is not needed due to constraints (length >= 1)
        # For a single element array, max_len starts at 1 and loop doesn't run, correctly returns 1.

        # handles edge cases
        # two pointer approach
        max_len = 1
        # simple approach
        # works fine
        current_len = 1

        for i in range(1, len(nums)):
            # hashmap approach
            if nums[i] > nums[i-1]:
                current_len += 1
            else:
                current_len = 1 # Reset if not strictly increasing

            max_len = max(max_len, current_len)

        return max_len
