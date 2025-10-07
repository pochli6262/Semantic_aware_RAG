S_1 = input()
S_2 = input()

# Create a list to represent the current grid.
grid = [list(S_1), list(S_2)]

# Directions for moving in the grid (down, up, right, left)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False]*2 for _ in range(2)]

# Find the coordinates of all black squares
black_squares = [(i, j) for i in range(2) for j in range(2) if grid[i][j] == '#']

# If there are fewer than 2 black squares, that violates constraints
if len(black_squares) < 2:
    print('No')
    exit()

from collections import deque
queue = deque()

# Start BFS from the first black square
queue.append(black_squares[0])
visited[black_squares[0][0]][black_squares[0][1]] = True

while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 2 and 0 <= ny < 2 and grid[nx][ny] == '#' and not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx, ny))

# Check if all black squares have been visited
if all(visited[x][y] for x, y in black_squares):
    print('Yes')
else:
    print('No')