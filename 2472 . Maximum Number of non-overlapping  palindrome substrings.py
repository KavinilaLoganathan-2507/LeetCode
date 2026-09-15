# You are given a string s and a positive integer k.

# Select a set of non-overlapping substrings from the string s that satisfy the following conditions:

# The length of each substring is at least k.
# Each substring is a palindrome.
# Return the maximum number of substrings in an optimal selection.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: s = "abaccdbbd", k = 3
# Output: 2
# Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
# It can be shown that we cannot find a selection with more than two valid substrings.
# Example 2:

# Input: s = "adbcda", k = 2
# Output: 0
# Explanation: There is no palindrome substring of length at least 2 in the string.

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        if k == 1: return n

        res = i = 0

        while i <= n - k:
            for d in (k, k + 1):
                if i + d <= n and s[i : i + d] == s[i : i + d][::-1]:
                    res += 1
                    i += d
                    break
            else:
                i += 1

        return res
