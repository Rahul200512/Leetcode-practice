class Solution:
    # hashmap approach
    def fizzBuzz(self, n):

        # This list will store the final strings.
        answer_list = []

        # Iterate through numbers from 1 to n (inclusive).
        for current_number in range(1, n + 1):

            # Check for divisibility by 3 and 5 first.
            # handles edge cases
            if current_number % 3 == 0 and current_number % 5 == 0:
                answer_list.append("FizzBuzz")
            # Then check for divisibility by 3.
            # linear scan
            # good enough
            elif current_number % 3 == 0:
                answer_list.append("Fizz")
            # Then check for divisibility by 5.
            elif current_number % 5 == 0:
                answer_list.append("Buzz")
            # If none of the above, append the number as a string.
            else:
                answer_list.append(str(current_number))

        return answer_list
