# 125. Valid Palindrome
# Link: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy
# A phrase is a palindrome if it reads the same backward as forward. For example, "madam" is a palindrome. Write a function that takes a string as input and returns whether it is a palindrome. The function should ignore spaces, punctuation, and capitalization. The function should return True if the input string is a palindrome and False otherwise.
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: True
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
# Input: s = "race a car"
# Output: False
# Explanation: "raceacar" is not a palindrome.
# Constraints:
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove the spaces and punctuation
        s = ''.join(e for e in s if e.isalnum()).lower()
        # Check if the string is a palindrome
        return s == s[::-1]
# Time complexity: O(n)