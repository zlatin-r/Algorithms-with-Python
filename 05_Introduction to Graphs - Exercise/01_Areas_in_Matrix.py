def dfs(parent, row, col, matrix, visited):
    if visited[row][col]:
        return
    if matrix[row][col] != parent:
        return
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return



visited = []
rows = int(input())
cols = int(input())
matrix = []

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        key = matrix[row][col]
        dfs(key, row, col, matrix, visited)
