rows = int(input())
cols = int(input())
matrix = []
visited = []

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

