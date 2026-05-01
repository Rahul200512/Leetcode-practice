class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        # Store frequency, first seen index, and last seen index for each number
        # data[num] = [frequency, first_index, last_index]
        data = {}
        for i, num in enumerate(nums):
            if num not in data:
                data[num] = [1, i, i] # first occurrence
            else:
                data[num][0] += 1     # increment frequency
                data[num][2] = i      # update last occurrence

        max_degree = 0
        min_length = float('inf') # Use infinity for initial comparison

        # Find the maximum frequency (degree of the array)
        for freq, _, _ in data.values():
            max_degree = max(max_degree, freq)
        
        # Iterate through numbers with max degree to find the shortest subarray
        for freq, first, last in data.values():
            if freq == max_degree:
                current_length = last - first + 1
                min_length = min(min_length, current_length)
                
        return min_length
