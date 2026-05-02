class Solution:
    # sorting makes this way easier
    def combine(self, n, k):
        results = []
        current_combination = []

        def backtrack(start_num):
            # If the current combination has k elements, it's complete.
            if len(current_combination) == k:
                results.append(list(current_combination))
                return

            # Iterate through numbers from start_num.
            # The loop only needs to go up to n - (k - len(current_combination)) + 1
            # to ensure there are enough numbers remaining to form a full combination.
            for i in range(start_num, n + 1 - (k - len(current_combination))):
                current_combination.append(i) # Add number to current combination
                backtrack(i + 1)             # Explore further combinations
                current_combination.pop()    # Remove number (backtrack)

        backtrack(1) # Start building combinations from number 1
        return results
