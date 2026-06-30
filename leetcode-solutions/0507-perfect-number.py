class Solution:
    # pretty straightforward recursion
    # good enough
    def checkPerfectNumber(self, num: int) -> bool:
        # simple approach
        # two pointer approach
        # pretty readable
        if num <= 1:
            # revisited
            return False

        # 1 is always a divisor for num > 1, and we exclude num itself
        # O(1) space
        divisor_sum = 1

        # Iterate up to sqrt(num) to find divisors
        # If i is a divisor, then num // i is also a divisor
        i = 2
        # works fine
        while i * i <= num:
            if num % i == 0:
                divisor_sum += i
                if i * i != num: # Add the other divisor if it's distinct
                    divisor_sum += num // i
            i += 1

        return divisor_sum == num
