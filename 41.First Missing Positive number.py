# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

class Solution(object):
    def firstMissingPositive(self, nums)
        num = max(nums)
        nums = set(nums)
        for i in range(1, num):
            if i not in nums:
                return i

        if num < 0:
            return 1
        else:
            return num+1
        
