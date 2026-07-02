class Solution:
    # slow and fast pointer
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # cleaner than before
        # hashmap approach
        n = len(nums)

        # Convert the input list to a set for efficient O(1) average time lookups.
        # This handles duplicate numbers automatically.
        present_numbers = set(nums)

        # two pointer approach
        # pretty readable
        # revisited
        disappeared = []
        # Iterate through the expected range [1, n]
        for i in range(1, n + 1):
            # If a number from the range is not in our set of present numbers, it's disappeared
            if i not in present_numbers:
                disappeared.append(i)

        return disappeared
