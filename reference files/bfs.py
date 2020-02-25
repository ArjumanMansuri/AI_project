def bfs(graph, start):
    closelist = []
    queue = [start]
    while len(queue) != 0:
        a = queue.pop(0)
        if a not in closelist:
            closelist.append(a)
            print(a)
            neighbours = graph[a]
            for n in neighbours:
                queue.append(n)


def bfs_shortestpath(graph, start, goal):
    visited = []
    # push first path in queue
    queue = [[start]]
    if start == goal:
        return "Your Goal is your start"
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path
        for i in graph.get(node):
            new_path = list(path)
            new_path.append(i)
            queue.append(new_path)


graph = {'A': ['B', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B', 'D'],
         'F': ['C'],
         'G': ['C']}
bfs(graph, 'A')
print(bfs_shortestpath(graph, 'A', 'D'))
