class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        
        # Keep dividing n by 2 until it's odd.
        while n % 2 == 0:
            n //= 2
            
        # If n becomes 1, it was a power of two.
        return n == 1
