def add_vertex(v):
    global vertices_no
    # global graph
    # global vertices
    if v in vertices:
        print("Vertex ", v, " already exists")
    else:
        vertices_no += 1
        vertices.append(v)
        if vertices_no>1:
            for vertex in graph:
                vertex.append(0)
        temp = []
        for i in range(vertices_no):
            temp.append(0)
        graph.append(temp)

def add_edge(v1, v2, w):
    global vertices_no
    # global graph
    # global vertices
    if v1 not in vertices:
        print("Vertex ", v1, " does not exist.")
    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")
    else:
        graph[v1-1][v2-1] = w

vertices = []

vertices_no = 0
graph = []

add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)

add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)

print("Internal representation: ", graph)