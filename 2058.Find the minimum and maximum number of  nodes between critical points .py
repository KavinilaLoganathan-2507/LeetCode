# A critical point in a linked list is defined as either a local maxima or a local minima.

# A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

# A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

# Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

# Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].

 

# Example 1:


# Input: head = [3,1]
# Output: [-1,-1]
# Explanation: There are no critical points in [3,1].
# Example 2:


# Input: head = [5,3,1,2,5,1,2]
# Output: [1,3]
# Explanation: There are three critical points:
# - [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
# - [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
# - [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
# The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
# The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.
# Example 3:


# Input: head = [1,3,2,2,3,2,2,2,7]
# Output: [3,3]
# Explanation: There are two critical points:
# - [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
# - [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
# Both the minimum and maximum distances are between the second and the fifth node.
# Thus, minDistance and maxDistance is 5 - 2 = 3.
# Note that the last node is not considered a local maxima because it does not have a next node.




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        min_distance = float('inf')
        first_index = -1
        prev_index = -1
        
        index = 1
        prev_node = head
        curr_node = head.next
        
        while curr_node and curr_node.next:
            nxt_val = curr_node.next.val
            curr_val = curr_node.val
            prev_val = prev_node.val
            
            # Check for local maxima or local minima
            if (curr_val > prev_val and curr_val > nxt_val) or \
               (curr_val < prev_val and curr_val < nxt_val):
                
                if first_index == -1:
                    first_index = index
                if prev_index != -1:
                    min_distance = min(min_distance, index - prev_index)
                
                prev_index = index
                
            prev_node = curr_node
            curr_node = curr_node.next
            index += 1
            
        # If fewer than 2 critical points exist
        if first_index == -1 or prev_index == first_index:
            return [-1, -1]
            
        max_distance = prev_index - first_index
        return [min_distance, max_distance]
