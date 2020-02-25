def dfsrec(visited, start):
    visited.append(start)
    print(start)
    neighbors = graph[start]
    for i in neighbors:
        if i not in visited:
            visited.append(i)
            dfsrec(visited, i)

def dfs(graph, start):
    visited = []
    dfsrec(visited, start)


graph = {'A': ['B', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B', 'E'],
         'E': ['A', 'B', 'D'],
         'F': ['C'],
         'G': ['C']}
dfs(graph, 'A')
