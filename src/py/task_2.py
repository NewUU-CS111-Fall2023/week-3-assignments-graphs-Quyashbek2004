def find_start_and_treasure(maze):
    start = None
    treasure = None

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == '@':
                start = (i, j)
            elif maze[i][j] == 'x':
                treasure = (i, j)

    return start, treasure

def is_valid_position(maze, i, j):
    if i < 0 or i >= len(maze) or j < 0 or j >= len(maze[0]):
        return False

    if maze[i][j] == '#':
        return False

    return True

def solve_maze(maze, j):
    start, treasure = find_start_and_treasure(maze)
    visited = [[-1] * len(maze[0]) for _ in range(len(maze))]
    visited[start[0]][start[1]] = j

    queue = deque([(start[0], start[1], j)])

    while queue:
        i, j, spikes_left = queue.popleft()

        if (i, j) == treasure:
            if spikes_left >= 1:
                print("SUCCESS")
                return

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj

            if is_valid_position(maze, ni, nj):
                if maze[ni][nj] == 's' and spikes_left >= 1:
                    if visited[ni][nj] < spikes_left - 1:
                        visited[ni][nj] = spikes_left - 1
                        queue.append((ni, nj, spikes_left - 1))
                elif visited[ni][nj] < spikes_left:
                    visited[ni][nj] = spikes_left
                    queue.append((ni, nj, spikes_left))

    print("IMPOSSIBLE")


n, m, j = map(int, input().split())

maze = []

for _ in range(n):
    maze.append(list(input()))

# Solve the maze
solve_maze(maze, j)
