#You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

#Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

#Example 1:

#Input: nums = [1,1,4,2,3], x = 5
#Output: 2
#Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
#Example 2:

#Input: nums = [5,6,7,8,9], x = 4
#Output: -1
#Example 3:

#Input: nums = [3,2,20,1,1,3], x = 10
#Output: 5
#Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.


class Solution:
    def minOperations(self, A: List[int], x: int) -> int:
        k = sum(A) - x
        if k < 0: return -1 
        best = -1
        
        s = i = 0
        
        for j, num in enumerate(A):
            s += num
            while s > k:
                s -= A[i]
                i += 1  
            if s == k:
                best = max(best, j - i + 1)

        return -1 if best < 0 else len(A) - best
