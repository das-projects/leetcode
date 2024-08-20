# 91. Decode Ways
# Link: https://leetcode.com/problems/decode-ways/
# Difficulty: Medium
# Description:
# A message containing letters from A-Z can be encoded into numbers using the following mapping:
# "1" -> 'A'
# "2" -> 'B'
# ...
# "26" -> 'Z'
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
# Given a string s consisting of digits, return the number of ways to decode it.
# The answer is guaranteed to fit in a 32-bit integer.
# Note: there may be strings that are impossible to decode
# Example 1:
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
# Example 3:
# Input: s = "0"
# Output: 0
# Explanation: There is no character that is mapped to a number starting with 0.
# The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of which start with 0.
# Hence, there are no valid ways to decode this since all digits need to be mapped.

# Constraints:
# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).

# Approach:
# 1. We will use dynamic programming to solve this problem.
# 2. We will create a dp array of size n+1 where n is the length of the string.
# 3. dp[i] will be the number of ways to decode the substring s[0...i].
# 4. We will initialize dp[0] as 1 as there is only one way to decode an empty string.
# 5. We will handle the edge cases where the first character is '0'.
# 6. If the first character is '0', we will set dp[1] as 0.
# 7. Otherwise, we will set dp[1] as 1.
# 8. We will iterate through the string and update the dp array based on the number of ways to decode the substring.
# 9. If the current character is '0', we will check if the previous character is '1' or '2'.
# 10. If the previous character is '1' or '2', we will set dp[i] as dp[i-2].
# 11. Otherwise, we will set dp[i] as 0.
# 12. If the current character is not '0', we will set dp[i] as dp[i-1].
# 13. If the current character and the previous character form a valid number, we will add dp[i-2] to dp[i].
# 14. Finally, we will return dp[n] where n is the length of the string.

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            one_digit = int(s[i - 1])
            two_digits = int(s[i - 2:i])

            if one_digit != 0:
                dp[i] += dp[i - 1]

            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[n]