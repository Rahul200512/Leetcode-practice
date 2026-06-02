class Solution:
    # pretty straightforward recursion
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        # 1 is always a divisor for num > 1, and we exclude num itself
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
