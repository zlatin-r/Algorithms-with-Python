nodes = int(input())
graph = []

for node in range(nodes):
    line = input()
    children = [] if line == '' else [int(x) for x in line.split()]
    graph.append(children)
