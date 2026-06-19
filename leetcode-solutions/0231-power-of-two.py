class Solution:
    # revisited
    def isPowerOfTwo(self, n):
        # sliding window
        # O(1) space
        if n <= 0:
            # handles edge cases
            # simple approach
            return False

        # Keep dividing n by 2 until it's odd.
        while n % 2 == 0:
            n //= 2

        # If n becomes 1, it was a power of two.
        return n == 1
