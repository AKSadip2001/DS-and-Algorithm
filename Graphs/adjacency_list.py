def add_vertex(v):
    global vertices_no
    if v in graph:
        print("Vertex ", v, " already exists.")
    else:
        vertices_no += 1
        graph[v] = []

def add_edge(v1, v2, edge_weight):
    if v1 not in graph:
        print("Vertex ", v1, "does not exist.")
    elif v2 not in graph:
        print("Vertex ", v2, "does not exist.")
    else:
        temp = [v2, edge_weight]
        graph[v1].append(temp)

graph = {}

vertices_no = 0
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)

add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)

print(graph)
