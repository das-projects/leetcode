# 76. Minimum Window Substring
# Link: https://leetcode.com/problems/minimum-window-substring/
# Difficulty: Hard
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
# Constraints:
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
# Follow up: Could you find an algorithm that runs in O(m + n) time?

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Sliding window approach
        n = len(s)
        m = len(t)
        if n < m:
            return ""
        # Count the characters in t
        charCount = [0] * 128
        for char in t:
            charCount[ord(char)] += 1
        # Initialize the window
        left = 0
        right = 0
        minLen = n + 1
        minStart = 0
        count = m
        while right < n:
            # If the character is in t then decrement the count
            if charCount[ord(s[right])] > 0:
                count -= 1
            # Decrement the character count
            charCount[ord(s[right])] -= 1
            right += 1
            while count == 0:
                # Update the minLen and minStart
                if right - left < minLen:
                    minLen = right - left
                    minStart = left
                # If the character is in t then increment the count
                charCount[ord(s[left])] += 1
                # If the character count is greater than 0 then increment the count
                if charCount[ord(s[left])] > 0:
                    count += 1
                left += 1
        # Return the minimum window substring
        return "" if minLen == n + 1 else s[minStart:minStart + minLen]