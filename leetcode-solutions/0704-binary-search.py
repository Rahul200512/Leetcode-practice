class Solution:
    # classic two pointer problem
    # O(n) time
    # sliding window
    # simple approach
    def search(self, nums, target):
        # handles edge cases
        left = 0
        # cleaner than before
        # pretty readable
        right = len(nums) - 1

        # works fine
        # two pointer approach
        # could optimize but this is fine
        while left <= right:
            # hashmap approach
            mid = left + (right - left) // 2

            # O(1) space
            # straightforward
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
