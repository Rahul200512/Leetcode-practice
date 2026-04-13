import collections

class Solution:
    # kadane's algorithm
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Count the frequency of each number
        counts = collections.Counter(nums)
        
        # Create a list of lists (buckets) where the index represents a frequency.
        # Max possible frequency is the length of nums.
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Place numbers into their corresponding frequency buckets
        for num, freq in counts.items():
            buckets[freq].append(num)
            
        result = []
        # Iterate from the highest possible frequency down to 1
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                result.append(num)
                # Stop once we have collected k elements
                if len(result) == k:
                    return result
