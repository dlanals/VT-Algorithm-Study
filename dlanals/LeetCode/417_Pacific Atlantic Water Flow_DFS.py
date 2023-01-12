'''
처음 작성한 코드가 좀 지저분해서 해당 코드는 solution을 많이 참고해서 작성한 최종 코드입니다.
일단 최종 코드 먼저 업로드하고, 처음 작성한 코드나 생각의 흐름 등은 다시 정리해서 올리도록 할게요! (시간관계상..)
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        def dfs(i: int, j: int, prev_height: int, coords: Set[Tuple[int]]) -> None:
            if i < 0 or i == m or j < 0 or j == n:
                # out of bounds
                return
            
            if (i, j) in coords:
                # already visited
                return
            
            height = heights[i][j]
            
            if height < prev_height:
                # water can't flow to a higher height
                return
            
            # ocean is reachable from current coordinate
            coords.add((i, j))
            
            # all four directions
            dfs(i + 1, j, height, coords)
            dfs(i - 1, j, height, coords)
            dfs(i, j + 1, height, coords)
            dfs(i, j - 1, height, coords)
            
        pacific_coords = set()
        
        # top row
        for j in range(n):
            dfs(0, j, 0, pacific_coords)
        
        # left col
        for i in range(m):
            dfs(i, 0, 0, pacific_coords)
            
        atlantic_coords = set()
            
        # right col
        for i in range(m):
            dfs(i, n - 1, 0, atlantic_coords)
            
        # bottom row
        for j in range(n):
            dfs(m - 1, j, 0, atlantic_coords)
