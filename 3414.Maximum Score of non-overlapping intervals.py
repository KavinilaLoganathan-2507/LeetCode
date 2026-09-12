# You are given a 2D integer array intervals, where intervals[i] = [li, ri, weighti]. Interval i starts at position li and ends at ri, and has a weight of weighti. You can choose up to 4 non-overlapping intervals. The score of the chosen intervals is defined as the total sum of their weights.

# Return the lexicographically smallest array of at most 4 indices from intervals with maximum score, representing your choice of non-overlapping intervals.

# Two intervals are said to be non-overlapping if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.

 

# Example 1:

# Input: intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]

# Output: [2,3]

# Explanation:

# You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

# Example 2:

# Input: intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]

# Output: [1,3,5,6]

# Explanation:

# You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = [(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)]
        arr.sort(key=lambda x: x[1])
        
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            l, r, w, idx = arr[i - 1]
            
            low, high = 1, i - 1
            prev = 0
            while low <= high:
                mid = (low + high) // 2
                if arr[mid - 1][1] < l:
                    prev = mid
                    low = mid + 1
                else:
                    high = mid - 1
                    
            for k in range(1, 5):
                skip_w, skip_idx = dp[i - 1][k]
                
                prev_w, prev_idx = dp[prev][k - 1]
                take_w = prev_w + w
                take_idx = sorted(prev_idx + [idx])
                
                if take_w > skip_w:
                    dp[i][k] = (take_w, take_idx)
                elif take_w == skip_w:
                    if take_idx < skip_idx:
                        dp[i][k] = (take_w, take_idx)
                    else:
                        dp[i][k] = (skip_w, skip_idx)
                else:
                    dp[i][k] = (skip_w, skip_idx)
                    
        return dp[n][4][1]
