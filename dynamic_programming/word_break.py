# 139. Word Break
# Link: https://leetcode.com/problems/word-break/
# Difficulty: Medium
# Description:
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
# Constraints:
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

# Approach:
# 1. We will use dynamic programming to solve this problem.
# 2. We will create a dp array of size n+1 where n is the length of the string.
# 3. dp[i] will be true if the substring s[0...i] can be segmented into words from the dictionary. Otherwise, it will be false. 
# 4. We will initialize dp[0] as true as the empty string can be segmented into words from the dictionary.
# 5. We will iterate through the string and check if the substring s[0...j] can be segmented into words from the dictionary and if the substring s[j+1...i] is in the dictionary.
# 6. If both the conditions are true, we will set dp[i] as true.
# 7. Finally, we will return dp[n] where n is the length of the string.

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Create a set of words from the dictionary
        memo = {}
        wordSet = set(wordDict)
        return self.dfs(s, wordSet, memo)
    
    def dfs(self, s, wordSet, memo):
        # If the string is in the memo, return the value
        if s in memo:
            return memo[s]
        # If the string is in the wordSet, return True
        if s in wordSet:
            return True
        # Iterate through the string and check if the prefix is in the wordSet and the suffix can be segmented into words from the dictionary
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix in wordSet and self.dfs(s[i:], wordSet, memo):
                memo[s] = True
                return True
        # If the string cannot be segmented into words from the dictionary, return False
        memo[s] = False
        return False
        