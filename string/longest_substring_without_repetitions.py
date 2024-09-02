# 3. Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium
# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Constraints:
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window approach
        n = len(s)
        maxLength = 0
        charIndex = [-1] * 128
        left = 0
        # right is the right pointer of the window
        # left is the left pointer of the window
        # right - left + 1 is the length of the window
        for right in range(n):
            # If the character at right pointer is already in the window then move the left pointer to the right of the last occurrence of the character
            if charIndex[ord(s[right])] >= left:
                left = charIndex[ord(s[right])] + 1
            # Update the index of the character at right pointer
            charIndex[ord(s[right])] = right
            # Update the maxLength
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength
