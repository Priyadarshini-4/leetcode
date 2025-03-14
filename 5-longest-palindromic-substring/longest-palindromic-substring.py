class Solution(object):
    def longestPalindrome(self, s):
        def expandAroundCenter(s, left, right):
            substring = ''  # Initialize substring
            max_length = 0   # Initialize max_length

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    max_length = right - left + 1  # Fix variable name
                    substring = s[left:right + 1]
                left -= 1
                right += 1
            return substring

        result = ''
        for i in range(len(s)):
            odd = expandAroundCenter(s, i, i)     # Fix function name
            even = expandAroundCenter(s, i, i + 1)

            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even

        return result
