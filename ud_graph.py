# Course: CS261 - Data Structures
# Author: Michael Hilmes
# Assignment: 6
# Description: Undirected Graph Implementation

from collections import deque

class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        Add new vertex to the graph
        """
        # If vertex is not already in the adj_list, add empty list to the dictionary
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u: str, v: str) -> None:
        """
        Add edge to the graph
        """
        # If the vertices are not equal...
        if u != v:
            # If vertex u is not in adj_list, add it
            if u not in self.adj_list:
                self.add_vertex(u)
            # If vertex v is not in adj_list, add it
            if v not in self.adj_list:
                self.add_vertex(v)
            # If vertex u does not have an edge to v, add it
            if v not in self.adj_list[u]:
                self.adj_list[u].append(v)
            # If vertex v does not have an edge to u, add it
            if u not in self.adj_list[v]:
                self.adj_list[v].append(u)
        

    def remove_edge(self, v: str, u: str) -> None:
        """
        Remove edge from the graph
        """
        # If both vertices v and u exist...
        if v in self.adj_list and u in self.adj_list:
            # If edge to u exists for vertex v, remove it
            if u in self.adj_list[v]:
                self.adj_list[v].remove(u)
            # If edge to v exists for vertex u, remove it
            if v in self.adj_list[u]:
                self.adj_list[u].remove(v)
        

    def remove_vertex(self, v: str) -> None:
        """
        Remove vertex and all connected edges
        """
        # If the vertex exists in adj_list, remove it
        self.adj_list.pop(v, None)
        # Check each remaining vertex and remove any edges connected to v
        for key in self.adj_list:
            if v in self.adj_list[key]:
                self.adj_list[key].remove(v)
        

    def get_vertices(self) -> []:
        """
        Return list of vertices in the graph (any order)
        """
        # Initialize empty list of vertices
        list_vertices = []
        # Iterate through adj_list and add the keys to list_vertices
        for key in self.adj_list:
            list_vertices.append(key)
        # Return the list of vertices
        return list_vertices

    def get_edges(self) -> []:
        """
        Return list of edges in the graph (any order)
        """
        # Initialize empty list to store edges
        list_edges = []
        # Iterate through the adj_list
        for key in self.adj_list:
            # For each edge associated with the given vertex key, create a sorted tuple representing the edge
            for item in self.adj_list[key]:
                edge = [key, item]
                edge.sort()
                edge_tuple = (edge[0], edge[1])
                # Add the edge to the list of edges
                list_edges.append(edge_tuple)
        # If the list of edges is non-empty, regenerate the list by calling set() to remove duplicates
        if len(list_edges) > 0:
            list_edges = list(set(list_edges))

        # Sort the list of edges and return it
        list_edges.sort()
        return list_edges

    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
        """
        # Initialize a counter and get the length of the path array
        count = 1
        length = len(path)

        # If the path is empty, return True
        if length == 0:
            return True

        # If the path has one vertex and the vertex exists, return True.
        # Return False if the vertex doesn't exist
        if length == 1:
            if path[0] in self.adj_list:
                return True
            else:
                return False

        # Check that all path vertices exist. If not, return False
        for item in path:
            if item not in self.adj_list:
                return False

        # Iterate through the path checking for valid connections from one vertex
        # to the next, returning False if a connection is not valid
        while count < length:
            if path[count] in self.adj_list[path[count - 1]]:
                return_val = True
                count += 1
            else:
                return_val = False
                break
        return return_val

       

    def dfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during DFS search
        Vertices are picked in alphabetical order
        """
        # Initialize lists for visited vertices and a stack
        visited = []
        stack = []
        # If starting vertex doesn't exist, return empty list
        if v_start not in self.adj_list:
            return visited
        # If v_end doesn't exist, set v_end to None
        if v_end is not None and v_end not in self.adj_list:
            v_end = None

        # Append the starting vertex to the stack
        stack.append(v_start)

        # Iterate while the stack is non-empty
        while len(stack) > 0:
            # Pop the top value off the stack
            pop_val = stack.pop()
            # Sort the edges in the pop_val vertex in reverse order
            temp_list = self.adj_list[pop_val]
            temp_list.sort()
            temp_list.reverse()
            # If pop_val vertex has not been visited, append it to the visited list
            if pop_val not in visited:
                visited.append(pop_val)
                # If we've reached the end specified by v_end, break out of loop
                if pop_val == v_end:
                    break
            # For each item in the sorted list of edges to vertices not yet visited, append to stack
            for item in temp_list:
                if item not in visited:
                    stack.append(item)
        # Return the list of visited vertices
        return visited


    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in alphabetical order
        """
        # Initialize empty lists for visited vertices and a queue
        visited = []
        queue = []
        # If starting vertex doesn't exist, return empty list
        if v_start not in self.adj_list:
            return visited
        # If v_end doesn't exist, set v_end to None
        if v_end is not None and v_end not in self.adj_list:
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
            temp_list = self.adj_list[dequeue]
            temp_list.sort()
            # Iterate through the list of edges adding vertices to the queue and
            # visited list if they haven't been visited.
            for item in temp_list:
                if item not in visited:
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

    def count_connected_components(self):
        """
        Return number of connected components in the graph
        """
        final_list = []

        if len(self.adj_list) == 0:
            return 0

        # For each vertex, run a depth first search to get a list of vertices for
        # that component, sort the list of vertices, and store in final_list as a tuple.
        for key in self.adj_list:
            dfs_list = self.dfs(key)
            dfs_list.sort()
            dfs_list = tuple(dfs_list)
            final_list.append(dfs_list)

        # Get the final count by finding the length of the list of unique, sorted dfs search results
        final_count = len(set(final_list))
        return final_count
      

    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        Receives: Nothing
        Returns: bool; True if cycle exists, False otherwise
        """
        # Find the length of the adjacency list, and get list of vertices
        length = len(self.adj_list)
        list_vertices = self.get_vertices()

        # Iterate through the range of the length of the adjacency list
        for i in range(0, length):
            # Initialize the first vertex, an empty list of visited vertices, and append first vertex
            vertex = list_vertices[i]
            visited = []
            visited.append(vertex)
            # Initialize empty queue
            queue = []
            # Append the first vertex and its parent to the queue (first vertex has no parent)
            queue.append((vertex, -1))

            while len(queue) > 0:
                # Dequeue the vertex, parent info from the queue
                (v, parent) = queue.pop(0)
                # Iterate through the vertices connected to the vertex
                for u in self.adj_list[v]:
                    # Append u to list of visited vertices, add u and its parent to the queue
                    if u not in visited:
                        visited.append(u)
                        queue.append((u, v))
                    # Return True if u is visited and is not a parent
                    elif u != parent:
                        return True

        return False


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = UndirectedGraph()
    print(g)

    for v in 'ABCDE':
        g.add_vertex(v)
    print(g)

    g.add_vertex('A')
    print(g)

    for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
        g.add_edge(u, v)
    print(g)


    print("\nPDF - method remove_edge() / remove_vertex example 1")
    print("----------------------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    g.remove_vertex('DOES NOT EXIST')
    g.remove_edge('A', 'B')
    g.remove_edge('X', 'B')
    print(g)
    g.remove_vertex('D')
    print(g)
    #
    #
    print("\nPDF - method get_vertices() / get_edges() example 1")
    print("---------------------------------------------------")
    g = UndirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    print(g.get_edges(), g.get_vertices(), sep='\n')
    #
    #
    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    for path in test_cases:
        print(list(path), g.is_valid_path(list(path)))
    #
    #
    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')
    #
    #
    print("\nPDF - method count_connected_components() example 1")
    print("---------------------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print(g.count_connected_components(), end=' ')
    print()
    #
    #
    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
        'add FG', 'remove GE')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())
