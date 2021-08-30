# Course: CS261 - Data Structures
# Author: Michael Hilmes
# Assignment: 6
# Description: Directed Graph Implementation

class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        Add vertex to the directed graph
        """
        # If vertices already exist, append a 0 to each vertex list
        if len(self.adj_matrix) > 0:
            for item in self.adj_matrix:
                item.append(0)
        # Add a new row of 0's to the adjacency matrix
        new_list = [0] * (self.v_count + 1)
        self.adj_matrix.append(new_list)
        # Increment the vertex count
        self.v_count += 1
        return self.v_count
        pass

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        Adds an edge to the graph
        """
        bounds = self.v_count - 1
        # If src or dst is out of bounds, do nothing and return
        if src > bounds or dst > bounds:
            return
        # If src is equal to dst, do nothing and return
        if src == dst:
            return
        # Add/update the weight at the given edge
        self.adj_matrix[src][dst] = weight
        pass

    def remove_edge(self, src: int, dst: int) -> None:
        """
        Remove the edge connecting the given source and destination vertices.
        Receives: src, dst as integers for source and destination vertices
        Returns: Nothing
        """
        bounds = self.v_count - 1
        # If src or dst is out of bounds, do nothing and return
        if src > bounds or dst > bounds:
            return
        if src < 0 or dst < 0:
            return
        # If src and dst are equal, do nothing and return
        if src == dst:
            return
        # Update the weight at the given edge to 0
        self.adj_matrix[src][dst] = 0
        pass

    def get_vertices(self) -> []:
        """
        Returns a list of the vertices in the graph.
        Receives: Nothing
        Returns: list_vertices as list of graph vertices
        """
        # Initialize empty list to store vertices
        list_vertices = []

        # If there are 0 vertices, return empty list
        if self.v_count == 0:
            return list_vertices
        # Append each vertex to the list of vertices
        for i in range(0, self.v_count):
            list_vertices.append(i)
        # Return the list of vertices
        return list_vertices
        pass

    def get_edges(self) -> []:
        """
        Returns a list of the the edges in the graph.
        Receives: Nothing
        Returns: list_edges as a list of the edges
        """
        # Initialize empty list to store edges
        list_edges = []
        # Iterate through each vertex
        for i in range(0, self.v_count):
            # Iterate through the list stored at the vertex
            for j in range(0, len(self.adj_matrix[i])):
                # If the edge exists from vertex i to j, create tuple of (i,j,weight)
                # and append it to the list of edges
                if self.adj_matrix[i][j] != 0:
                    edge = (i, j, self.adj_matrix[i][j])
                    list_edges.append(edge)
        # Return the list of edges
        return list_edges
        pass

    def is_valid_path(self, path: []) -> bool:
        """
        Determine if the given path is valid. Returns True if so, otherwise False.
        Receives: path as list of vertices
        Returns: bool, with True indicating a valid path
        """
        # Initialize a counter and get the length of the path array
        count = 1
        length = len(path)
        list_vertices = self.get_vertices()

        # If the path is empty, return True
        if length == 0:
            return True
        # If the path has one vertex and the vertex exists, return True.
        # Return False if the vertex doesn't exist
        if length == 1:
            if path[0] in list_vertices:
                return True
            else:
                return False

        # Check that all path vertices exist. If not, return False
        for item in path:
            if item not in list_vertices:
                return False

        # Iterate through the path checking for valid connections from one vertex
        # to the next, returning False if a connection is not valid
        while count < length:
            value = self.adj_matrix[path[count - 1]][path[count]]
            if value > 0:
                return_val = True
                count += 1
            else:
                return_val = False
                break

        # Return True if path is valid, False if not
        return return_val

        pass

    def dfs(self, v_start, v_end=None) -> []:
        """
        Breadth first search for the directed graph.
        Receives: v_start and v_end as indices representing start and end points
        Returns: visited as list of visited vertices
        """
        # Initialize lists for visited vertices, an empty stack, and find the list of vertices
        visited = []
        stack = []
        pre_stack = []
        list_vertices = self.get_vertices()
        # If starting vertex doesn't exist, return empty list
        if v_start not in list_vertices:
            return visited
        # If v_end doesn't exist, set v_end to None
        if v_end is not None and v_end not in list_vertices:
            v_end = None

        # Append the starting vertex to the stack
        stack.append(v_start)

        # Iterate while the stack is non-empty
        while len(stack) > 0:
            pre_stack = []
            # Pop the top value off the stack
            pop_val = stack.pop()
            temp_list = self.adj_matrix[pop_val]

            if pop_val not in visited:
                visited.append(pop_val)
                # If we've reached the end specified by v_end, break out of loop
                if pop_val == v_end:
                    break

            for i in range(0, len(temp_list)):
                if i not in visited and temp_list[i] != 0:
                    pre_stack.append(i)
                    pre_stack.sort()
                    pre_stack.reverse()
            for item in pre_stack:
                stack.append(item)

        return visited
        pass

    def bfs(self, v_start, v_end=None) -> []:
        """
        Breadth first search for the directed graph.
        Receives: v_start and v_end as indices representing start and end points
        Returns: visited as list of visited vertices
        """
        # Initialize empty lists for visited vertices and a queue
        visited = []
        queue = []
        list_vertices = self.get_vertices()
        # If starting vertex doesn't exist, return empty list
        if v_start not in list_vertices:
            return visited
        # If v_end doesn't exist, set v_end to None
        if v_end is not None and v_end not in list_vertices:
            v_end = None

        # Append the starting vertex to the queue and list of visited vertices
        queue.append(v_start)
        visited.append(v_start)
        # If the start and end vertices are the same, return the list
        if v_start == v_end:
            return visited
        # Iterate while the queue is non-empty
        while len(queue) > 0:
            # Dequeue and sort the list of edges
            dequeue = queue.pop(0)
            temp_list = self.adj_matrix[dequeue]
            # Iterate through the list of edges adding vertices to the queue and
            # visited list if they haven't been visited.
            for item in range(0, len(temp_list)):
                if item not in visited and temp_list[item] !=0:
                    visited.append(item)
                    queue.append(item)
                    # Break out of the loop if the end has been reached
                    if v_end in visited:
                        break
            # Break out of the loop if the end has been reached
            if v_end in visited:
                break
        # Return the list of visited vertices
        return visited
        pass

    def helper_dfs(self, i, visited, helper):
        """
        Helper method to use DFS to find cycle.
        **Note**: Found this algorithm on youtube nETSETOS channel and modified it
        Receives: i as index; visited as list of visited vertices; helper as list of vertices
        Returns: True if cyclic; False if acyclic
        """
        visited[i] = True
        helper[i] = True
        neighbors = self.adj_matrix[i]
        # Iterate through the vertices associated with vertex i
        for k in range(0, len(neighbors)):
            # Determine if vertex k is a neighbor of i
            if neighbors[k] > 0:
                curr = k
                # If curr is being encountered a second time, a cycle has been detected
                if helper[curr] == True:
                    return True
                # If curr vertex hasn't been visited, recursively call helper_dfs
                if visited[curr] == False:
                    answer = self.helper_dfs(curr, visited, helper)
                    # Return True if cycle is detected
                    if answer == True:
                        return True
        # If vertex is not being encountered again, then there is not a cycle. Backtrack.
        helper[i] = False
        # Return False if no cycle is found
        return False

    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        **Note**: Found this algorithm on youtube nETSETOS channel and modified it
        Receives: Nothing
        Returns: bool; True if cycle exists, False otherwise
        """
        # Create arrays to store whether node has been visited and a helper
        # array to determine if the vertex has been visited twice, making it a cycle
        visited = [False] * self.v_count
        helper = [False] * self.v_count
        # Iterate through the range of available vertices
        for i in range(0, self.v_count):
            # If vertex has not been visited, call helper_dfs to determine if cyclic
            if visited[i] == False:
                answer = self.helper_dfs(i, visited, helper)
                if answer == True:
                    return True
        # Return False if no cycle is found
        return False


        # # Previous attempt
        #
        # # Find the number of vertices, and get list of vertices
        # length = self.v_count
        # list_vertices = self.get_vertices()
        #
        # for i in range(0, length):
        #     # Initialize the first vertex, an empty list of visited vertices, and append first vertex
        #     vertex = i
        #     visited = []
        #     visited.append(vertex)
        #     # Initialize empty queue
        #     queue = []
        #     # Append the first vertex and its parent to the queue (first vertex has no parent)
        #     queue.append((vertex, -1))
        #
        #     while len(queue) > 0:
        #         if len(queue) > 1:
        #             (v, parent) = queue.pop()
        #         else:
        #         # Dequeue the vertex, parent info from the queue
        #             (v, parent) = queue.pop(0)
        #         # Iterate through the vertices connected to the vertex
        #         for u in range(0,len(self.adj_matrix[v])):
        #             temp = self.adj_matrix[v][u]
        #             if self.adj_matrix[v][u] != 0:
        #                 # Append u to list of visited vertices, add u and its parent to the queue
        #                 if u not in visited:
        #                     if len(queue) == 0:
        #                         visited.append(u)
        #                     queue.append((u, v))
        #                 # Return True if u is visited and is not a parent
        #                 elif u != parent:
        #                     return True
        # return False

        pass

    def dijkstra(self, src: int) -> []:
        """
        Implements Dijkstra's algorithm to return the path of
        shortest length/cost to all vertices in the graph.
        Receives: src as int for the source vertex
        Returns: list of shortest length/cost
        """
        visited = {}
        queue = []
        dfs = self.dfs(src)
        for i in range(0, self.v_count):
            if i not in dfs:
                visited[i] = float('inf')
        queue.append((0 , src))
        while len(queue) > 0:
            (d, v) = queue.pop(0)
            if v not in visited:
                visited[v] = d
            for i in range(len(self.adj_matrix[v])):
                if self.adj_matrix[v][i] > 0:
                    queue.append((d + self.adj_matrix[v][i], i))
                    queue.sort()
                if len(visited) == self.v_count:
                    new_list = [0] * self.v_count
                    for key in range(0, self.v_count):
                        new_list[key] = visited[key]
                    break

        return new_list


        pass


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = DirectedGraph()
    print(g)
    for _ in range(5):
        g.add_vertex()
    print(g)

    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    for src, dst, weight in edges:
        g.add_edge(src, dst, weight)
    print(g)


    print("\nPDF - method get_edges() example 1")
    print("----------------------------------")
    g = DirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    print(g.get_edges(), g.get_vertices(), sep='\n')
    #
    #
    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))
    #
    #
    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for start in range(0,5):
        print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')

    print("\nPDF - method dfs() and bfs() example 2")
    print("--------------------------------------")
    edges = [(0,10,1),(2,6,1),(3,0,1),(3,1,1),(3,6,1),(4,7,1),(4,12,1),(6,4,1),(7,12,1),(8,2,1),(10,0,1),(11,3,1)]
    g = DirectedGraph(edges)
    for start in range(3, 5):
        print(f'{start} DFS:{g.dfs(start)}')
    #
    #
    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)
    #
    #
    print("\nPDF - dijkstra() example 1")
    print("--------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    g.remove_edge(4, 3)
    print('\n', g)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
