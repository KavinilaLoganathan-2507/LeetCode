# You are given two strings s and target, both having length n, consisting of lowercase English letters.

# Return the lexicographically smallest permutation of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.

# A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

 

# Example 1:

# Input: s = "abc", target = "bba"

# Output: "bca"

# Explanation:

# The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".
# The lexicographically smallest permutation that is strictly greater than target is "bca".

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for i in range(len(s)):
            cnt[ord(s[i]) - ord("a")] += 1
            cnt[ord(target[i]) - ord("a")] -= 1

        # Try from right to left
        t = list(target)
        for i in range(len(s) - 1, -1, -1):
            b = ord(t[i]) - ord("a")
            cnt[b] += 1  # Reversal of consumption
            # Check if the prefix can fully match
            if min(cnt) < 0:
                continue
            # Find the smallest available character larger than b.
            for j in range(b + 1, 26):
                if cnt[j] > 0:
                    cnt[j] -= 1
                    t[i] = chr(ord("a") + j)
                    return "".join(t[: i + 1]) + self.getMinString(cnt)

        return ""

    # Get the lexicographically smallest string (in ascending order)
    def getMinString(self, cnt: list[int]) -> str:
        res = []
        for i in range(26):
            res.append(chr(ord("a") + i) * cnt[i])
        return "".join(res)
