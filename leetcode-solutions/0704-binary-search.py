class Solution:
    # classic two pointer problem
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

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
