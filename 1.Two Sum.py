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
