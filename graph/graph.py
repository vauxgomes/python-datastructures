#!/usr/bin/env python

""" Digraph class """

__author__ = "Vaux Gomes"
__copyright__ = "Copyright 2020, Vaux Gomes"
__credits__ = ["Vaux Gomes"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Vaux Gomes"
__email__ = "vauxgomes@gmail.com"
__status__ = "Production"


class Digraph:
    def __init__(self):
        self.__nodes = {}
        self.__vertices = []

    def get_vertices(self):
        return self.__vertices

    def get_size(self):
        return len(self.__vertices)

    def add_vertex(self, vertex):
        if vertex not in self.__vertices:
            self.__vertices.append(vertex)

        if vertex not in self.__nodes:
            self.__nodes[vertex] = {}

    def add_edge(self, i, j, w=1, bidirected=False):
        # Adding possibly unknown vertices
        self.add_vertex(i)
        self.add_vertex(j)

        # Addind edge
        if j not in self.__nodes[i]:
            self.__nodes[i][j] = [w]
        else:
            self.__nodes[i][j].append(w)

        if bidirected:
            self.add_edge(j, i, w)

    def dijkstra(self, u, v):
        '''
            Note: This function considers only the weight of the first edged
        '''

        unvisited = self.__vertices.copy()
        visited = []

        # Let all distances be Infinite (None)
        matrix = {i: {'distance': None, 'prev': None} for i in self.__vertices}

        # Let distance of start vertex from start vertex = 0
        matrix[u]['distance'] = 0

        # Repeat until all vertices be visited
        while unvisited:
            # Visit the unvisited vextex with the smallest known distance from the start vertex
            smallest_distance_vextex = unvisited[0]
            smallest_distance = matrix[smallest_distance_vextex]['distance']

            for i in unvisited:
                if matrix[i]['distance'] is not None and (smallest_distance is None or matrix[i]['distance'] < smallest_distance):
                    smallest_distance_vextex = i
                    smallest_distance = matrix[smallest_distance_vextex]['distance']
            
            unvisited.remove(smallest_distance_vextex)

            # For the current vertex, calculate distance of each neighbour
            neighbours = self.__nodes[smallest_distance_vextex].keys()

            for n in neighbours:
                total = smallest_distance + self.__nodes[smallest_distance_vextex][n][0]
                
                # Update distance if smaller than current
                if matrix[n]['distance'] is None or matrix[n]['distance'] > total:
                    matrix[n]['distance'] = total
                    matrix[n]['prev'] = smallest_distance_vextex

            # Add current vertex to list of visited
            visited.append(smallest_distance_vextex)

        # Path
        path = []
        curr = v

        while matrix[curr]['prev'] != None:
            path.insert(0, matrix[curr]['prev'])
            curr = matrix[curr]['prev']

        path.append(matrix[v]["distance"])

        # Return
        return path

    def __str__(self):
        ''' Print in graphviz style '''
        return 'Digraph G {{\n\trankdir="LR"; \n\t{}\n \n\t{} \n}}'.format('\n\t'.join(
            [f'{i} -> {j} [label="{k}"]'
                for i in self.__nodes.keys()
                for j in self.__nodes[i].keys()
                for k in self.__nodes[i][j]
             ]),
            '\n\t'.join([f'{i}[shape="circle"]' for i in self.__vertices])
        )


if __name__ == '__main__':
    d = Digraph()

    d.add_edge('A', 'B', 6)
    d.add_edge('A', 'D', 1)
    d.add_edge('B', 'C', 5)
    d.add_edge('D', 'B', 2)
    d.add_edge('D', 'E', 1)
    d.add_edge('E', 'B', 2)
    d.add_edge('E', 'C', 5)

    print(d)

    print('DIJKSTRA')
    print('FROM: A')
    print('TO: C')
    print(' -> '.join([str(i) for i in d.dijkstra('A', 'C')]))
