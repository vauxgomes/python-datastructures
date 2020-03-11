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