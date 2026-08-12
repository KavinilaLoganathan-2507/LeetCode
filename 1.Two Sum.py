# You are given an array of integers nums and an integer target. Return the indices of the two numbers such that they add up to target.

# You may assume that each input has exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

#________________________________________________________________________________________________________________________________________________________________________

# class Solution:
 #     def twoSum(self, nums: List[int], target: int) -> List[int]:
user_input = input("Enter numbers separated by spaces (e.g., 2 7 11 15): ")
nums= [int(x) for x in user_input.split()]
target = int(input("Enter the target sum : "))
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  
    
    # class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     hashmap = {}  # value -> index
        
    #     for i, val in enumerate(nums):
    #         needed = target - val
    #         if needed in hashmap:
    #             return [hashmap[needed], i]
    #         hashmap[val] = i
