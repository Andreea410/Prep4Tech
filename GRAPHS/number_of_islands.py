# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3  

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) < 1:
            return 0
    
        visited = set()
        rows , cols = len(grid) , len(grid[0])
        nr_islands = 0

        def bfs(row , col):
            q = collections.deque()
            q.append((row,col))
            visited.add((row,col))

            while q:
                r , c = q.popleft()
                directions = [[-1,0],[1,0],[0,-1],[0,1]]
                for dr , dc in directions:
                    current_r, current_c = r + dr, c + dc

                    if current_r in range(rows) and current_c in range(cols) and grid[current_r][current_c] == "1" and (current_r , current_c) not in visited:
                        q.append((current_r,current_c))
                        visited.add((current_r,current_c)) 
                    

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    nr_islands +=1
                    bfs(i,j)
        return nr_islands
