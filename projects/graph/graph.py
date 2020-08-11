"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.

        """
        #pass  # TODO
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        #pass  # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist!!!!")
        

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        pass  # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #pass  # TODO
        q = Queue()
        q.enqueue(starting_vertex)
        #print(q)

        visited = set()
        #print(q.size())

        while q.size() > 0:
            #print(q.size())
            v = q.dequeue()
            #print(v)

            if v not in visited:
                visited.add(v)
                #print(visited)
                
                print(v)

                for next_vertex in self.get_neighbors(v):
                    q.enqueue(next_vertex)
                    #print(next_vertex)

        #print(visited)
        #return visited


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #pass  # TODO

        s = Stack()
        s.push(starting_vertex)
        #print(q)

        visited = set()
        #print(q.size())

        while s.size() > 0:
            #print(q.size())
            v = s.pop()
            #print(v)

            if v not in visited:
                visited.add(v)
                #print(visited)
                
                print(v)

                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)
                    #print(next_vertex)

        #print(visited)
        #return visited

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
    ## inclass live code
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)

        for v in self.get_neighbors(starting_vertex):
            if v not in visited:
                self.dft_recursive(v, visited)







    #     #pass  # TODO
    #     #s = Stack()
    #     #s.push(starting_vertex)
    #     #print(q)

    #     visited = set()
    #     #print(visited)
    #     #print(q.size())

    #     self.helper_dft_recursive(starting_vertex, visited)

    # def helper_dft_recursive(self, starting_vertex, visited_set):
    #     if starting_vertex in visited_set:
    #         return
        
    #     visited_set.add(starting_vertex)
    #     print(starting_vertex)
    #     for next_vertex in self.get_neighbors(starting_vertex):
    #         self.helper_dft_recursive(next_vertex, visited_set)




        # while s.size() > 0:
        #     #print(q.size())
        #     v = s.pop()
        #     #print(v)

        #     if v not in visited:
        #         visited.add(v)
        #         #print(visited)
                
        #         print(v)

        #         for next_vertex in self.get_neighbors(v):
        #             s.push(next_vertex)
        #             #print(next_vertex)

        #print(visited)
        #return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO
        q = Queue()
        # equeuing the PATH
        #queue can store a list of nodes
        q.enqueue([starting_vertex])
        #print(q)

        visited = set()
        #print(q.size())

        while q.size() > 0:
            #print(q.size())
            v = q.dequeue()
            #print(v)
            #print(v[-1])

            if v[-1] not in visited:
                if v[-1] == destination_vertex:
                    print("FOUND IT")
                    #print(v)
                    return v
                visited.add(v[-1])
                #print(visited)
                
                #print(v)

                for next_vertex in self.get_neighbors(v[-1]):
                    new_path = v.copy()
                    #need to make a copy

                    # new_path = v

                    ## adding to the path every time you dequeue
                    new_path.append(next_vertex)
                    q.enqueue(new_path)
                    #print(new_path)
                    #print(next_vertex)

        

    



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

        s = Stack()
        # equeuing the PATH
        #queue can store a list of nodes
        s.push([starting_vertex])
        #print(q)

        visited = set()
        #print(q.size())

        while s.size() > 0:
            #print(q.size())
            v = s.pop()
            #print(v)
            #print(v[-1])

            if v[-1] not in visited:
                if v[-1] == destination_vertex:
                    print("FOUND IT")
                    #print(v)
                    return v
                visited.add(v[-1])
                #print(visited)
                
                #print(v)

                for next_vertex in self.get_neighbors(v[-1]):
                    new_path = v.copy()
                    #need to make a copy

                    # new_path = v

                    ## adding to the path every time you dequeue
                    new_path.append(next_vertex)
                    s.push(new_path)
                    #print(new_path)
                    #print(next_vertex)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()
        path = [starting_vertex]

        new_path = self.dfs_recursive_helper(starting_vertex, destination_vertex, visited, path)
        print("NEW PATH")
        print(new_path)
        return new_path


    def dfs_recursive_helper(self, starting_vertex, destination_vertex, visited_set, path):
        #print(f'visited set: {visited_set}')
        #path = [starting_vertex]
        if path[-1] not in visited_set:
            if path[-1] == destination_vertex:
                print("FOUND IT")
                print(path)
                return path
            visited_set.add(path[-1])
            for next_vertex in self.get_neighbors(path[-1]):
                new_path = path.copy()
                new_path.append(next_vertex)
                #print(new_path)
                self.dfs_recursive_helper(next_vertex, destination_vertex, visited_set, new_path)
        ## go down this path
        return path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    #print(graph.get_neighbors(2))

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print(f"Breadth First Traversal: {graph.bft(1)}")
    

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(f"Depth First Traversal: {graph.dft(1)}")
    print("Recursive DFT:")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))

    print("DFS RECURSIVE")
    print(graph.dfs_recursive(1, 6))
    graph.dfs_recursive(1, 6)