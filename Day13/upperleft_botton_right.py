# Unstop 100 Days of Code
# Day 13
# upperleft botton right

from collections import deque

def user_logic(n, m, grid):
    """
    Finds each connected component (water body) of 1s and returns
    its upper-left cell and bottom-right cell.
    
    Upper-left: min row, then min col (min(cells))
    Bottom-right: max row, then max col (max(cells))
    """
    visited = [[False] * m for _ in range(n)]
    result = []
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                # BFS to find the whole water body (connected component)
                queue = deque([(i, j)])
                visited[i][j] = True
                cells = []
                
                while queue:
                    r, c = queue.popleft()
                    cells.append((r, c))
                    
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m:
                            if not visited[nr][nc] and grid[nr][nc] == 1:
                                visited[nr][nc] = True
                                queue.append((nr, nc))
                
                # Upper-left: smallest (row, col)
                r1, c1 = min(cells)
                # Bottom-right: largest (row, col)
                r2, c2 = max(cells)
                
                result.append([r1, c1, r2, c2])
    
    # Sort water bodies by their upper-left cell
    result.sort(key=lambda x: (x[0], x[1]))
    return result


def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    grid = []
    index = 2
    for i in range(n):
        row = list(map(int, input_data[index:index + m]))
        grid.append(row)
        index += m
    
    result = user_logic(n, m, grid)
    
    for res in result:
        print(" ".join(map(str, res)))

if __name__ == "__main__":
    main()