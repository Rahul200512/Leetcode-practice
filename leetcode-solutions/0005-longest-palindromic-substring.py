class Solution:
    # union find would also work here
    def longestPalindrome(self, s: str) -> str:
        # According to constraints, s will always have at least one character.
        # Initialize with the first character, as it's the shortest possible palindrome.
        longest_palindrome_substring = s[0] 
        
        # Helper function to expand outwards from a given center(s)
        # It takes initial left and right pointers.
        def expand_around_center(left, right):
            # Expand as long as characters match and indices are within bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # The palindrome found is from index (left + 1) to (right - 1).
            # Python slice [start:end] includes start but excludes end.
            # So, s[left + 1 : right] is the correct substring.
            return s[left + 1 : right]

        # Iterate through each character in the string
        for i in range(len(s)):
            # Case 1: Palindromes with odd length
            # The current character s[i] is the single center.
            odd_palindrome = expand_around_center(i, i)
            if len(odd_palindrome) > len(longest_palindrome_substring):
                longest_palindrome_substring = odd_palindrome

            # Case 2: Palindromes with even length
            # The center is between s[i] and s[i+1].
            even_palindrome = expand_around_center(i, i + 1)
            if len(even_palindrome) > len(longest_palindrome_substring):
                longest_palindrome_substring = even_palindrome
        
        return longest_palindrome_substring
