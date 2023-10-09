def bfs(graph, start):
    visited.append(start)
    queue.append(start)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

visited = []
queue = []

graph = {'5' : ['3','7'],'3' : ['2', '4'],'7' : ['8'],'2' : [],'4' : ['8'],'8' : []}
print("Following is Breadth First Traversal: ")
bfs(graph, '5')