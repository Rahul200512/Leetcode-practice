class Solution:
    def twoSum(self, nums, target):
        
        # Store numbers we've seen and their indices
        seen_numbers = {} 
        
        for current_index, current_number in enumerate(nums):
            complement = target - current_number
            
            # Check if the complement needed is already in our map
            if complement in seen_numbers:
                # If yes, we found the pair
                return [seen_numbers[complement], current_index]
            
            # If not, add the current number and its index to the map
            seen_numbers[current_number] = current_index
