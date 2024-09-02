# 424. Longest Repeating Character Replacement
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/
# Difficulty: Medium
# Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string. 
# Return the maximum length of the substring containing the same letter you can get after performing the above operations.
# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# Constraints:
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window approach
        n = len(s)
        maxLength = 0
        charCount = [0] * 26
        left = 0
        maxCharCount = 0
        for right in range(n):
            # The window size is the maximum character count + k
            charCount[ord(s[right]) - ord('A')] += 1
            maxCharCount = max(maxCharCount, charCount[ord(s[right]) - ord('A')])
            # If the window size is greater than the maximum character count + k then shrink the window
            if right - left + 1 > maxCharCount + k:
                charCount[ord(s[left]) - ord('A')] -= 1
                left += 1
            # Update the maxLength
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength