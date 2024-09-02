# 5. Longest Palindromic Substring
# Link: https://leetcode.com/problems/longest-palindromic-substring/
# Difficulty: Medium
# Given a string s, return the longest palindromic substring in s.
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        start = 0
        end = 0
        for i in range(n):
            # Check for odd length palindrome
            len1 = self.expandAroundCenter(s, i, i)
            # Check for even length palindrome
            len2 = self.expandAroundCenter(s, i, i + 1)
            maxLen = max(len1, len2)
            if maxLen > end - start:
                start = i - (maxLen - 1) // 2
                end = i + maxLen // 2
        return s[start:end + 1]
    
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1