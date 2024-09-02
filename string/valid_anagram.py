# 242. Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Given two strings s and t, return true if t is an anagram of s, and false otherwise. 
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charCount = [0] * 26
        # Count the characters in s and t
        for char in s:
            # ord(char) - ord('a') will give the index of the character in the charCount array
            charCount[ord(char) - ord('a')] += 1
        for char in t:
            charCount[ord(char) - ord('a')] -= 1
        # If the character count is not zero then return False
        for count in charCount:
            if count != 0:
                return False
        return True