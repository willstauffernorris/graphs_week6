class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

vertices = {}
def add_vertex(vertex):
    vertices[vertex] = set()


## I'm reversing the edges from the other examples: 
## I want each vertex to point to its ancestor
def add_edge(v1, v2):
    if v1 in vertices and v2 in vertices:
        vertices[v2].add(v1)


## get neighbors
def get_neighbors(vertex_id):
    return vertices[vertex_id]

# import a Stack
def earliest_ancestor(ancestors, starting_node):
    # 'ancestors' is a list of ancestors




    ## basically I want to visit every node in the list of ancestors
    ## return the node that is the **farthest** away from the 'starting node'
    ## I think this means that I'm going to use a Depth First Traversal

    s = Stack()
    visited = set()

    s.push([starting_node])

    if get_neighbors(starting_node) == set():
        print("NO VERTEX FOUND")
        return -1


    while s.size() > 0:

        path = s.pop()
        vertex = path[-1]
        print(f'visited: {visited}')
        

        if vertex not in visited:
            visited.add(vertex)
            print(visited)

            #print(get_neighbors(vertex))
            # if get_neighbors(vertex) == set():
            #     print("NO VERTEX FOUND")
            #     return -1

            for next_vertex in get_neighbors(vertex):
                print(next_vertex)
            
                new_path = path.copy()

                new_path.append(next_vertex)
                s.push(new_path)
                print(new_path)

    return new_path[-1]

                ## edge cases:
                 ## if there is a tie, return the ancestor with the lowest numeric value
                 ## if 'starting node' has no parents, return -1


    

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

#self.assertEqual(earliest_ancestor(test_ancestors, 1), 10)
for item in test_ancestors:
    add_vertex(item[0])
    add_vertex(item[1])

for item in test_ancestors:
    add_edge(item[0], item[1])

    ## maybe I don't need to explicitly make the edges and vertices
    ## but I don't know how else do to it, so I'm gonna try



print(vertices)
print(earliest_ancestor(test_ancestors, 1))
print(earliest_ancestor(test_ancestors, 2))
print(earliest_ancestor(test_ancestors, 3))
