graph = [
    [3, 6],
    [3, 6, 4, 2, 5],
    [1, 4, 5],
    [5, 0, 1],
    [1, 2, 6],
    [2, 1, 3],
    [0, 1, 4]
]

visited = [False] * len(graph)

for node in graph:
    dfs(node, graph, visited)
