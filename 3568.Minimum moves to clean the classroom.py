# You are given an m x n grid classroom where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:

# 'S': Starting position of the student
# 'L': Litter that must be collected (once collected, the cell becomes empty)
# 'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)
# 'X': Obstacle the student cannot pass through
# '.': Empty space
# You are also given an integer energy, representing the student's maximum energy capacity. The student starts with this energy from the starting position 'S'.

# Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area 'R', which resets the energy to its maximum capacity energy.

# Return the minimum number of moves required to collect all litter items, or -1 if it's impossible.

 

# Example 1:

# Input: classroom = ["S.", "XL"], energy = 2

# Output: 2

# Explanation:

# The student starts at cell (0, 0) with 2 units of energy.
# Since cell (1, 0) contains an obstacle 'X', the student cannot move directly downward.
# A valid sequence of moves to collect all litter is as follows:
# Move 1: From (0, 0) → (0, 1) with 1 unit of energy and 1 unit remaining.
# Move 2: From (0, 1) → (1, 1) to collect the litter 'L'.
# The student collects all the litter using 2 moves. Thus, the output is 2.
# Example 2:

# Input: classroom = ["LS", "RL"], energy = 4

# Output: 3

# Explanation:

# The student starts at cell (0, 1) with 4 units of energy.
# A valid sequence of moves to collect all litter is as follows:
# Move 1: From (0, 1) → (0, 0) to collect the first litter 'L' with 1 unit of energy used and 3 units remaining.
# Move 2: From (0, 0) → (1, 0) to 'R' to reset and restore energy back to 4.
# Move 3: From (1, 0) → (1, 1) to collect the second litter 'L'.
# The student collects all the litter using 3 moves. Thus, the output is 3.
# Example 3:

# Input: classroom = ["L.S", "RXL"], energy = 3

# Output: -1

# Explanation:

# No valid path collects all 'L'.



from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        id = [[-1] * n for _ in range(m)]

        k = 0
        sr = 0
        sc = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr = r
                    sc = c
                elif classroom[r][c] == 'L':
                    id[r][c] = k
                    k += 1

        if k == 0:
            return 0

        total_mask = (1 << k) - 1

        best = [
            [
                [-1] * (1 << k)
                for _ in range(n)
            ]
            for _ in range(m)
        ]

        queue = deque()

        best[sr][sc][0] = energy
        queue.append((sr, sc, 0, energy, 0))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c, mask, e, moves = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                ne = e - 1

                if ne < 0:
                    continue

                nmask = mask

                if classroom[nr][nc] == 'R':
                    ne = energy

                if classroom[nr][nc] == 'L':
                    nmask |= 1 << id[nr][nc]

                if nmask == total_mask:
                    return moves + 1

                if ne <= best[nr][nc][nmask]:
                    continue

                best[nr][nc][nmask] = ne

                queue.append((nr, nc, nmask, ne, moves + 1))

        return -1
