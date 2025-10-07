S1 = input()
S2 = input()

black_squares = [(0, 0) if S1[0] == '#' else None,
                (0, 1) if S1[1] == '#' else None,
                (1, 0) if S2[0] == '#' else None,
                (1, 1) if S2[1] == '#' else None]
black_squares = [sq for sq in black_squares if sq is not None]

# Function to check if we can connect all black squares
from collections import deque
visited = set()
queue = deque([black_squares[0]])

while queue:
    x, y = queue.popleft()
    visited.add((x, y))
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) in black_squares and (nx, ny) not in visited:
            queue.append((nx, ny))

if len(visited) == len(black_squares):
    print("Yes")
else:
    print("No")