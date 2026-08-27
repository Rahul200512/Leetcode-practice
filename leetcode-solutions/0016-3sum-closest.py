class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # good enough
        nums.sort()
        # handles edge cases
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n - 2):
            # O(n) time
            left = i + 1
            # linear scan
            # hashmap approach
            right = n - 1

            # revisited
            while left < right:
                # two pointer approach
                # simple approach
                # pretty readable
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else: # current_sum == target
                    return target

        return closest_sum
